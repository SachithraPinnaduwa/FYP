# FYP Test Generator - VS Code Extension

AI-Powered Unit Test Generator for Python using Adaptive Prompting. This extension integrates with the backend server to generate comprehensive unit tests for your Python code.

## Features

### 📁 Select a Python File
Select a Python file from your workspace to generate unit tests for it.

### 🧠 Adaptive Prompting
Uses AI-powered test planning to analyze code structure and generate better test coverage:
1. **Static Analysis** - Extracts code structure (functions, classes, docstrings)
2. **AI Test Planning** - Determines what to test (edge cases, error handling)
3. **Test Generation** - Fine-tuned model generates the actual test code

### 💾 Save & Copy Results
Generated tests can be copied to the clipboard or saved directly to a file from the results panel.

## Requirements

- **Backend Server**: The extension requires the backend server to be running. Start it with:
  ```bash
  cd backend
  python backend.py
  ```
  The server runs on `http://localhost:5000` by default.

- **Python Files**: The extension works with Python files (`.py`)

## Extension Commands

Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and type:

| Command | Description |
|---------|-------------|
| `FYP: Select Python Files and Generate Tests` | Select a Python file to generate tests |

## Keyboard Shortcuts

| Shortcut | Command |
|----------|---------|
| `Ctrl+Alt+T` / `Cmd+Alt+T` | Select a Python file to generate tests |

## How It Works

1. **Invoke Command**: Press `Ctrl+Alt+T` or use the Command Palette
2. **Select a Python File**: Choose a single Python file from your workspace
3. **Optional Description**: Add a description to guide test generation (e.g., specific edge cases)
4. **Choose Mode**: Select between Adaptive Prompting (recommended) or Basic Generation
5. **View Results**: Generated tests appear in a webview panel next to your code
6. **Save or Copy**: Save tests to a file or copy them to your clipboard

## Backend Endpoints Used

| Endpoint | Description |
|----------|-------------|
| `/health` | Check backend availability |
| `/generate-tests` | Basic test generation |
| `/generate-tests-adaptive` | Adaptive prompting test generation |

## Known Issues

- Backend server must be running before using the extension
- Large files may take longer to process
- The model has a context window limit; very large files may need to be split

## Release Notes

### 0.0.1

- Simplified workspace integration
- Single command structure for cleaner user experience
- Native adaptive prompting test-generation

---

**Enjoy generating tests!** 🧪
