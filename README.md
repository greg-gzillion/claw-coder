# 🦞 TX CLAW - AI Assistant for TX Blockchain & PhoenixPME

## Features
- Indexes 27,966+ code files from TX blockchain
- Indexes 1,233+ documentation files
- Uses 3 specialized AI models:
  - **Llama 3.2** (2GB) - Fast chat & questions
  - **Codellama 7B** (3.8GB) - Code explanation
  - **DeepSeek Coder** (3.8GB) - Code generation

## Commands
- `ask <question>` - Ask about TX/PhoenixPME
- `analyze <file>` - Deep code analysis
- `generate <desc>` - Generate Rust code
- `docsearch <term>` - Search documentation
- `codesearch <term>` - Search codebase
- `prices` - Metal prices
- `status` - System status
- `chat` - Interactive mode

## Setup
1. Install Ollama: `curl -fsSL https://ollama.com/install.sh | sh`
2. Pull models: `ollama pull llama3.2:3b codellama:7b deepseek-coder:6.7b`
3. Run claw: `./claw`

## Requirements
- Ollama running locally
- Python 3.10+
- 10GB free space for models
