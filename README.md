# CLAW - PhoenixPME AI Assistant

CLAW is a command-line AI assistant for the PhoenixPME blockchain project.

## Setup

### 1. Get Groq API Key (Free)

Visit https://console.groq.com
- Sign up with Google/GitHub
- Create an API key at https://console.groq.com/keys
- Copy the key (starts with gsk_)

### 2. Install Dependencies

pip3 install groq

### 3. Set API Key

export GROQ_API_KEY="gsk_your_key_here"

### 4. Run CLAW

./claw

## Commands

ask <question>  - Ask about your codebase
search <term>   - Search all files
status          - Show system status
token           - Show TESTUSD info
exit            - Quit
