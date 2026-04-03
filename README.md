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

## 🤖 AI Model Setup

Claw-Coder supports multiple AI models for different tasks. Heres how to set them up:

### Required Models (Pick One or More)

| Model | Size | Best For | Command |
|-------|------|----------|---------|
| **Llama 3.2** | 2GB | Fast chat, general questions | `ollama pull llama3.2:3b` |
| **Codellama 7B** | 3.8GB | Code explanation, understanding | `ollama pull codellama:7b` |
| **DeepSeek Coder** | 3.8GB | Code generation, complex tasks | `ollama pull deepseek-coder:6.7b` |

### Installation Options

#### Option 1: Install All Models (9.6GB total)
```bash
ollama pull llama3.2:3b
ollama pull codellama:7b
ollama pull deepseek-coder:6.7b
```

#### Option 2: Install Only Chat Model (2GB - Fastest)
```bash
ollama pull llama3.2:3b
```

#### Option 3: Install Code Models Only (7.6GB)
```bash
ollama pull codellama:7b      # Code explanation
ollama pull deepseek-coder:6.7b  # Code generation
```

### Verify Models are Installed
```bash
ollama list
```

You should see:
```
NAME                   ID              SIZE
llama3.2:3b            a80c4f17acd5    2.0 GB
codellama:7b           8fdf8f752f6e    3.8 GB
deepseek-coder:6.7b    ce298d984115    3.8 GB
```

### Test a Model
```bash
# Test chat model
ollama run llama3.2:3b "Hello, what is TX blockchain?"

# Test code model
ollama run codellama:7b "Explain this Rust code: fn main() {}"

# Test generation model
ollama run deepseek-coder:6.7b "Write a Rust function to calculate collateral"
```

### Model Configuration

The `model_config.json` file maps commands to models:
```json
{
  "chat": "llama3.2:3b",
  "explain": "codellama:7b",
  "generate": "deepseek-coder:6.7b"
}
```

### Remove Models (Free Space)
```bash
ollama rm codellama:7b        # Remove specific model
ollama list                    # See whats left
```
