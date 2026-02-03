# FYP Test Generator - VS Code Extension

AI-Powered Unit Test Generator for Python using Adaptive Prompting. This extension integrates with the backend server to generate comprehensive unit tests for your Python code.

## Features

### 🧪 Generate Tests for Active File
Generate unit tests for the currently open Python file with a single command or keyboard shortcut.

### 📁 Select Multiple Python Files
Select multiple Python files from your workspace and generate tests for all of them at once.

### 🧠 Adaptive Prompting
Uses AI-powered test planning to analyze code structure and generate better test coverage:
1. **Static Analysis** - Extracts code structure (functions, classes, docstrings)
2. **AI Test Planning** - Determines what to test (edge cases, error handling)
3. **Test Generation** - Fine-tuned model generates the actual test code

### 🔍 Code Structure Analysis
Analyze Python code to understand its structure before generating tests.

### 💾 Save & Copy Results
Generated tests can be copied to clipboard or saved directly to a file.

## Requirements

- **Backend Server**: The extension requires the backend server to be running. Start it with:
  ```bash
  cd backend
  python app.py
  ```
  The server runs on `http://localhost:5000` by default.

- **Python Files**: The extension works with Python files (`.py`)

## Extension Commands

Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type:

| Command | Description |
|---------|-------------|
| `FYP: Select Python Files and Generate Tests` | Select multiple Python files to generate tests |
| `FYP: Generate Tests for Active File` | Generate tests for the currently open file |
| `FYP: Analyze Code Structure` | Analyze the structure of the current file |
| `FYP: Configure Backend URL` | Change the backend server URL |

## Keyboard Shortcuts

| Shortcut | Command |
|----------|---------|
| `Ctrl+Shift+T` / `Cmd+Shift+T` | Generate tests for active file |
| `Ctrl+Alt+T` / `Cmd+Alt+T` | Select files and generate tests |

## Extension Settings

This extension contributes the following settings:

| Setting | Default | Description |
|---------|---------|-------------|
| `fypTestGenerator.backendUrl` | `http://localhost:5000` | URL of the backend server |
| `fypTestGenerator.useAdaptivePrompting` | `true` | Use AI-powered adaptive prompting |
| `fypTestGenerator.maxTokens` | `512` | Maximum tokens to generate per request |

## Context Menu

Right-click on a Python file in the editor or explorer to access:
- **FYP: Generate Tests for Active File**
- **FYP: Analyze Code Structure**

## How It Works

1. **Select Python Files**: Choose one or more Python files from your workspace
2. **Optional Description**: Add a description to guide test generation
3. **Choose Mode**: Select between Adaptive Prompting (recommended) or Basic Generation
4. **View Results**: Generated tests appear in a webview panel
5. **Save or Copy**: Save tests to a file or copy to clipboard

## Backend Endpoints Used

| Endpoint | Description |
|----------|-------------|
| `/health` | Check backend availability |
| `/generate-tests` | Basic test generation |
| `/generate-tests-adaptive` | Adaptive prompting test generation |
| `/analyze-code` | Static code analysis |

## Known Issues

- Backend server must be running before using the extension
- Large files may take longer to process
- The model has a context window limit; very large files may need to be split

## Release Notes

### 0.0.1

Initial release:
- Select Python files and generate tests
- Generate tests for active file
- Adaptive prompting support
- Code structure analysis
- Configurable backend URL
- Keyboard shortcuts
- Context menu integration

---

**Enjoy generating tests!** 🧪

## Working with Markdown

You can author your README using Visual Studio Code.  Here are some useful editor keyboard shortcuts:

* Split the editor (`Cmd+\` on macOS or `Ctrl+\` on Windows and Linux)
* Toggle preview (`Shift+Cmd+V` on macOS or `Shift+Ctrl+V` on Windows and Linux)
* Press `Ctrl+Space` (Windows, Linux, macOS) to see a list of Markdown snippets

## For more information

* [Visual Studio Code's Markdown Support](http://code.visualstudio.com/docs/languages/markdown)
* [Markdown Syntax Reference](https://help.github.com/articles/markdown-basics/)

**Enjoy!**
