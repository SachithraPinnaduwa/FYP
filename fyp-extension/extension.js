// VS Code Extension for AI-Powered Unit Test Generation
import * as vscode from 'vscode';

// Backend endpoints
const BACKEND_BASE = 'http://localhost:5000';
const GENERATE_TESTS_URL = `${BACKEND_BASE}/generate-tests`;
const GENERATE_ADAPTIVE_URL = `${BACKEND_BASE}/generate-tests-adaptive`;
const ANALYZE_CODE_URL = `${BACKEND_BASE}/analyze-code`;
const GENERATE_INTENTIONS_URL = `${BACKEND_BASE}/generate-intentions`;
const HEALTH_URL = `${BACKEND_BASE}/health`;

/**
 * Extract clean test code from model response.
 * @param {string} responseText - Raw response from the model
 * @returns {string} - Extracted test code
 */
function extractTestCode(responseText) {
    if (!responseText) return '';
    
    let text = responseText.trim();
    
    // Try to find Python code blocks first
    const codeBlockPatterns = [
        /```python\s*([\s\S]*?)\s*```/g,
        /```\s*([\s\S]*?)\s*```/g,
        /~~~python\s*([\s\S]*?)\s*~~~/g,
        /~~~\s*([\s\S]*?)\s*~~~/g,
    ];
    
    for (const pattern of codeBlockPatterns) {
        const matches = [...text.matchAll(pattern)];
        if (matches.length > 0) {
            // Find the match that contains unittest
            for (const match of matches) {
                const code = match[1];
                if (code.includes('unittest') || code.includes('TestCase') || code.includes('def test_')) {
                    return code.trim();
                }
            }
            // If no unittest match, return the longest match
            return matches.reduce((a, b) => a[1].length > b[1].length ? a : b)[1].trim();
        }
    }
    
    // Look for unittest code without code blocks
    const lines = text.split('\n');
    const codeLines = [];
    let inCode = false;
    
    for (const line of lines) {
        if (line.includes('import unittest') || (line.trim().startsWith('class ') && line.includes('Test'))) {
            inCode = true;
        }
        
        if (inCode) {
            if (line.trim().startsWith('#') && line.trim().length > 100) {
                continue;
            }
            if (['explanation:', 'note:', 'output:'].some(marker => line.toLowerCase().includes(marker))) {
                break;
            }
            codeLines.push(line);
        }
    }
    
    if (codeLines.length > 0) {
        const result = codeLines.join('\n').trim();
        if (result.includes('unittest') || result.includes('TestCase')) {
            return result;
        }
    }
    
    // Final fallback
    if (text.includes('import unittest') || text.includes('class Test')) {
        return text;
    }
    
    return '';
}

/**
 * Check if backend is reachable
 * @returns {Promise<boolean>}
 */
async function checkBackendHealth() {
    try {
        const response = await fetch(HEALTH_URL, { 
            method: 'GET',
            signal: AbortSignal.timeout(5000)
        });
        return response.ok;
    } catch {
        return false;
    }
}

/**
 * Generate tests for code using the backend
 * @param {string} code - Python code to test
 * @param {string} description - Optional description
 * @param {boolean} useAdaptive - Use adaptive prompting
 * @param {number} maxTokens - Max tokens to generate
 * @returns {Promise<{tests: string, error?: string, structureSummary?: string, intentions?: object}>}
 */
async function generateTests(code, description = '', useAdaptive = true, maxTokens = 512) {
    const url = useAdaptive ? GENERATE_ADAPTIVE_URL : GENERATE_TESTS_URL;
    const payload = {
        code,
        description,
        max_new_tokens: maxTokens,
        include_debug: false,
    };
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
            signal: AbortSignal.timeout(180000), // 3 minute timeout
        });
        
        if (!response.ok) {
            const error = await response.text();
            return { tests: '', error: `HTTP ${response.status}: ${error}` };
        }
        
        /** @type {{tests?: string, error?: string, structure_summary?: string, intentions?: object}} */
        const result = await response.json();
        if (result.error) {
            return { tests: '', error: result.error };
        }
        
        const tests = extractTestCode(result.tests || '') || result.tests || '';
        return { 
            tests, 
            structureSummary: result.structure_summary,
            intentions: result.intentions 
        };
    } catch (err) {
        const errorMessage = err instanceof Error ? err.message : String(err);
        return { tests: '', error: errorMessage };
    }
}

/**
 * Analyze code structure using backend
 * @param {string} code - Python code to analyze
 * @returns {Promise<{structure: object|null, summary: string, error?: string}>}
 */
async function analyzeCode(code) {
    try {
        const response = await fetch(ANALYZE_CODE_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code }),
            signal: AbortSignal.timeout(30000),
        });
        
        if (!response.ok) {
            const error = await response.text();
            return { structure: null, summary: '', error: `HTTP ${response.status}: ${error}` };
        }
        
        /** @type {{structure?: object, summary?: string}} */
        const result = await response.json();
        return { structure: result.structure || null, summary: result.summary || '' };
    } catch (err) {
        const errorMessage = err instanceof Error ? err.message : String(err);
        return { structure: null, summary: '', error: errorMessage };
    }
}

/**
 * Get all Python files in the workspace
 * @returns {Promise<vscode.Uri[]>}
 */
async function getPythonFilesInWorkspace() {
    const files = await vscode.workspace.findFiles('**/*.py', '**/node_modules/**');
    return files;
}

/**
 * Create webview panel for displaying results
 * @param {vscode.ExtensionContext} context
 * @param {string} title
 * @param {string} content
 */
function createResultsPanel(context, title, content) {
    const panel = vscode.window.createWebviewPanel(
        'testResults',
        title,
        vscode.ViewColumn.Beside,
        { enableScripts: true }
    );
    
    panel.webview.html = getWebviewContent(content);
    return panel;
}

/**
 * Generate HTML content for webview
 * @param {string} testCode
 * @returns {string}
 */
function getWebviewContent(testCode) {
    const escapedCode = testCode
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Tests</title>
    <style>
        body {
            font-family: var(--vscode-font-family);
            padding: 20px;
            background-color: var(--vscode-editor-background);
            color: var(--vscode-editor-foreground);
        }
        h1 {
            color: var(--vscode-titleBar-activeForeground);
            border-bottom: 1px solid var(--vscode-panel-border);
            padding-bottom: 10px;
        }
        pre {
            background-color: var(--vscode-textCodeBlock-background);
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid var(--vscode-panel-border);
        }
        code {
            font-family: var(--vscode-editor-font-family);
            font-size: var(--vscode-editor-font-size);
        }
        .actions {
            margin-top: 20px;
        }
        button {
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            border: none;
            padding: 8px 16px;
            margin-right: 10px;
            cursor: pointer;
            border-radius: 3px;
        }
        button:hover {
            background-color: var(--vscode-button-hoverBackground);
        }
        .info {
            background-color: var(--vscode-inputValidation-infoBackground);
            border: 1px solid var(--vscode-inputValidation-infoBorder);
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>🧪 Generated Unit Tests</h1>
    <div class="info">
        <strong>Tip:</strong> Click "Copy to Clipboard" or "Save as File" to use these tests.
    </div>
    <pre><code>${escapedCode}</code></pre>
    <div class="actions">
        <button onclick="copyToClipboard()">📋 Copy to Clipboard</button>
        <button onclick="saveFile()">💾 Save as File</button>
    </div>
    <script>
        const vscode = acquireVsCodeApi();
        const testCode = ${JSON.stringify(testCode)};
        
        function copyToClipboard() {
            navigator.clipboard.writeText(testCode).then(() => {
                vscode.postMessage({ command: 'copied' });
            });
        }
        
        function saveFile() {
            vscode.postMessage({ command: 'save', code: testCode });
        }
    </script>
</body>
</html>`;
}

/**
 * Main command: Select Python files and generate tests
 * @param {vscode.ExtensionContext} context
 */
async function selectFilesAndGenerateTests(context) {
    // Check backend health first
    const isHealthy = await vscode.window.withProgress(
        { location: vscode.ProgressLocation.Notification, title: 'Checking backend connection...' },
        () => checkBackendHealth()
    );
    
    if (!isHealthy) {
        const action = await vscode.window.showErrorMessage(
            'Cannot connect to the backend server. Make sure it is running on http://localhost:5000',
            'Retry',
            'Cancel'
        );
        if (action === 'Retry') {
            return selectFilesAndGenerateTests(context);
        }
        return;
    }
    
    // Get all Python files in workspace
    const pythonFiles = await getPythonFilesInWorkspace();
    
    if (pythonFiles.length === 0) {
        vscode.window.showWarningMessage('No Python files found in the workspace.');
        return;
    }
    
    // Let user select files
    const items = pythonFiles.map(file => ({
        label: vscode.workspace.asRelativePath(file),
        uri: file,
        picked: false,
    }));
    
    const selected = await vscode.window.showQuickPick(items, {
        canPickMany: true,
        placeHolder: 'Select Python files to generate tests for',
        title: 'Select Python Files',
    });
    
    if (!selected || selected.length === 0) {
        return;
    }
    
    // Ask for optional description
    const description = await vscode.window.showInputBox({
        prompt: 'Enter an optional description for test generation (press Enter to skip)',
        placeHolder: 'e.g., Focus on edge cases and error handling',
    });
    
    // Ask for generation mode
    const modeChoice = await vscode.window.showQuickPick(
        [
            { label: '🧠 Adaptive Prompting', description: 'AI-powered test planning (recommended)', value: true },
            { label: '⚡ Basic Generation', description: 'Direct test generation', value: false },
        ],
        { placeHolder: 'Select generation mode' }
    );
    
    if (!modeChoice) return;
    const useAdaptive = modeChoice.value;
    
    // Generate tests with progress
    await vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: 'Generating unit tests...',
            cancellable: true,
        },
        async (progress, token) => {
            const results = [];
            const total = selected.length;
            
            for (let i = 0; i < selected.length; i++) {
                if (token.isCancellationRequested) break;
                
                const file = selected[i];
                progress.report({ 
                    message: `Processing ${file.label} (${i + 1}/${total})`,
                    increment: (100 / total)
                });
                
                try {
                    const document = await vscode.workspace.openTextDocument(file.uri);
                    const code = document.getText();
                    
                    const result = await generateTests(code, description || '', useAdaptive);
                    results.push({
                        file: file.label,
                        ...result,
                    });
                } catch (err) {
                    results.push({
                        file: file.label,
                        tests: '',
                        error: err.message,
                    });
                }
            }
            
            // Display results
            if (results.length === 1) {
                // Single file - show in webview
                const result = results[0];
                if (result.error) {
                    vscode.window.showErrorMessage(`Failed to generate tests: ${result.error}`);
                } else if (result.tests) {
                    const panel = createResultsPanel(context, `Tests for ${result.file}`, result.tests);
                    
                    panel.webview.onDidReceiveMessage(async message => {
                        if (message.command === 'copied') {
                            vscode.window.showInformationMessage('Tests copied to clipboard!');
                        } else if (message.command === 'save') {
                            const uri = await vscode.window.showSaveDialog({
                                defaultUri: vscode.Uri.file(`test_${result.file}`),
                                filters: { 'Python': ['py'] }
                            });
                            if (uri) {
                                await vscode.workspace.fs.writeFile(uri, Buffer.from(message.code, 'utf8'));
                                vscode.window.showInformationMessage(`Tests saved to ${uri.fsPath}`);
                            }
                        }
                    });
                }
            } else {
                // Multiple files - merge results
                const successResults = results.filter(r => r.tests && !r.error);
                const failedFiles = results.filter(r => r.error).map(r => r.file);
                
                if (successResults.length === 0) {
                    vscode.window.showErrorMessage('Failed to generate tests for all selected files.');
                    return;
                }
                
                // Merge all test code
                let mergedCode = '"""Auto-generated unit tests"""\nimport unittest\n\n';
                
                for (const result of successResults) {
                    mergedCode += `# Tests for ${result.file}\n`;
                    mergedCode += result.tests + '\n\n';
                }
                
                mergedCode += "\nif __name__ == '__main__':\n    unittest.main()\n";
                
                const panel = createResultsPanel(context, 'Generated Tests', mergedCode);
                
                if (failedFiles.length > 0) {
                    vscode.window.showWarningMessage(`Could not generate tests for: ${failedFiles.join(', ')}`);
                }
                
                panel.webview.onDidReceiveMessage(async message => {
                    if (message.command === 'copied') {
                        vscode.window.showInformationMessage('Tests copied to clipboard!');
                    } else if (message.command === 'save') {
                        const uri = await vscode.window.showSaveDialog({
                            defaultUri: vscode.Uri.file('test_generated.py'),
                            filters: { 'Python': ['py'] }
                        });
                        if (uri) {
                            await vscode.workspace.fs.writeFile(uri, Buffer.from(message.code, 'utf8'));
                            vscode.window.showInformationMessage(`Tests saved to ${uri.fsPath}`);
                        }
                    }
                });
            }
        }
    );
}

/**
 * Generate tests for the currently active file
 * @param {vscode.ExtensionContext} context
 */
async function generateTestsForActiveFile(context) {
    const editor = vscode.window.activeTextEditor;
    
    if (!editor) {
        vscode.window.showWarningMessage('No active editor found.');
        return;
    }
    
    const document = editor.document;
    
    if (document.languageId !== 'python') {
        vscode.window.showWarningMessage('The active file is not a Python file.');
        return;
    }
    
    // Check backend health
    const isHealthy = await vscode.window.withProgress(
        { location: vscode.ProgressLocation.Notification, title: 'Checking backend connection...' },
        () => checkBackendHealth()
    );
    
    if (!isHealthy) {
        vscode.window.showErrorMessage('Cannot connect to the backend server. Make sure it is running on http://localhost:5000');
        return;
    }
    
    const code = document.getText();
    const fileName = vscode.workspace.asRelativePath(document.uri);
    
    // Generate with progress
    await vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: `Generating tests for ${fileName}...`,
            cancellable: false,
        },
        async () => {
            const result = await generateTests(code, '', true);
            
            if (result.error) {
                vscode.window.showErrorMessage(`Failed to generate tests: ${result.error}`);
                return;
            }
            
            if (result.tests) {
                const panel = createResultsPanel(context, `Tests for ${fileName}`, result.tests);
                
                panel.webview.onDidReceiveMessage(async message => {
                    if (message.command === 'copied') {
                        vscode.window.showInformationMessage('Tests copied to clipboard!');
                    } else if (message.command === 'save') {
                        const baseName = fileName.replace('.py', '');
                        const uri = await vscode.window.showSaveDialog({
                            defaultUri: vscode.Uri.file(`test_${baseName}.py`),
                            filters: { 'Python': ['py'] }
                        });
                        if (uri) {
                            await vscode.workspace.fs.writeFile(uri, Buffer.from(message.code, 'utf8'));
                            vscode.window.showInformationMessage(`Tests saved to ${uri.fsPath}`);
                        }
                    }
                });
            }
        }
    );
}

/**
 * Analyze code structure of the active file
 * @param {vscode.ExtensionContext} context
 */
async function analyzeActiveFile(context) {
    const editor = vscode.window.activeTextEditor;
    
    if (!editor) {
        vscode.window.showWarningMessage('No active editor found.');
        return;
    }
    
    const document = editor.document;
    
    if (document.languageId !== 'python') {
        vscode.window.showWarningMessage('The active file is not a Python file.');
        return;
    }
    
    const code = document.getText();
    
    await vscode.window.withProgress(
        {
            location: vscode.ProgressLocation.Notification,
            title: 'Analyzing code structure...',
            cancellable: false,
        },
        async () => {
            const result = await analyzeCode(code);
            
            if (result.error) {
                vscode.window.showErrorMessage(`Analysis failed: ${result.error}`);
                return;
            }
            
            if (result.summary) {
                vscode.window.showInformationMessage(result.summary, { modal: true });
            }
        }
    );
}

/**
 * Configure backend URL
 */
async function configureBackend() {
    const config = vscode.workspace.getConfiguration('fypTestGenerator');
    const currentUrl = config.get('backendUrl', BACKEND_BASE);
    
    const newUrl = await vscode.window.showInputBox({
        prompt: 'Enter the backend server URL',
        value: currentUrl,
        placeHolder: 'http://localhost:5000',
    });
    
    if (newUrl) {
        await config.update('backendUrl', newUrl, vscode.ConfigurationTarget.Global);
        vscode.window.showInformationMessage(`Backend URL updated to: ${newUrl}`);
    }
}

/**
 * Extension activation
 * @param {vscode.ExtensionContext} context
 */
export function activate(context) {
    console.log('FYP Test Generator extension is now active!');
    
    // Register commands
    const selectFilesCommand = vscode.commands.registerCommand(
        'fyp-extension.selectFilesAndGenerateTests',
        () => selectFilesAndGenerateTests(context)
    );
    
    const generateForActiveCommand = vscode.commands.registerCommand(
        'fyp-extension.generateTestsForActiveFile',
        () => generateTestsForActiveFile(context)
    );
    
    const analyzeCommand = vscode.commands.registerCommand(
        'fyp-extension.analyzeCode',
        () => analyzeActiveFile(context)
    );
    
    const configureCommand = vscode.commands.registerCommand(
        'fyp-extension.configureBackend',
        () => configureBackend()
    );
    
    // Legacy hello world command (can be removed)
    const helloCommand = vscode.commands.registerCommand(
        'fyp-extension.helloWorld',
        () => vscode.window.showInformationMessage('FYP Test Generator Extension is active!')
    );
    
    context.subscriptions.push(
        selectFilesCommand,
        generateForActiveCommand,
        analyzeCommand,
        configureCommand,
        helloCommand
    );
}

/**
 * Extension deactivation
 */
export function deactivate() {
    console.log('FYP Test Generator extension deactivated.');
}
