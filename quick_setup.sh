#!/bin/bash
# Ultra-quick setup for fresh laptop

echo "🦞 Quick Claw-Coder Setup"

# Clone
git clone https://github.com/greg-gzillion/claw-coder.git
cd claw-coder

# Install minimal dependencies
pip3 install requests

# Run status check
./status.sh

echo "✅ Ready! For full features: ./install.sh"
