#!/bin/bash
# Model Setup Script for Claw-Coder

echo "🤖 Claw-Coder Model Setup"
echo "========================="
echo ""

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/tags &>/dev/null; then
    echo "⚠️  Ollama is not running. Starting it..."
    ollama serve &
    sleep 3
fi

echo "Select models to install:"
echo "  1) Chat only (2GB - Llama 3.2)"
echo "  2) Code only (7.6GB - Codellama + DeepSeek)"
echo "  3) All models (9.6GB - Full setup)"
echo "  4) Custom selection"
echo "  5) Skip (use existing)"
echo ""
read -p "Choice (1-5): " choice

case $choice in
    1)
        echo "📦 Installing Llama 3.2 (2GB)..."
        ollama pull llama3.2:3b
        ;;
    2)
        echo "📦 Installing Codellama 7B (3.8GB)..."
        ollama pull codellama:7b
        echo "📦 Installing DeepSeek Coder (3.8GB)..."
        ollama pull deepseek-coder:6.7b
        ;;
    3)
        echo "📦 Installing all models (9.6GB)..."
        ollama pull llama3.2:3b
        ollama pull codellama:7b
        ollama pull deepseek-coder:6.7b
        ;;
    4)
        echo "Custom selection:"
        read -p "Install Llama 3.2? (y/n): " install_llama
        read -p "Install Codellama? (y/n): " install_codellama
        read -p "Install DeepSeek? (y/n): " install_deepseek
        [[ $install_llama == "y" ]] && ollama pull llama3.2:3b
        [[ $install_codellama == "y" ]] && ollama pull codellama:7b
        [[ $install_deepseek == "y" ]] && ollama pull deepseek-coder:6.7b
        ;;
    5)
        echo "Skipping model installation"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

echo ""
echo "✅ Models installed:"
ollama list

echo ""
echo "Test a model:"
echo "  ollama run llama3.2:3b \"Hello\""
