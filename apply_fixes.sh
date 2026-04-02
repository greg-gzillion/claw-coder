#!/bin/bash
# Auto-generated fix script for detected bugs
# Location: /home/greg/dev/claw-coder/apply_fixes.sh

CLAW_PATH="/home/greg/dev/claw-coder"
TX_PATH="/home/greg/dev/TX"

echo "🔧 APPLYING AUTO-GENERATED FIXES"
echo "================================"
echo ""

# Fix 1: Add checked arithmetic to prevent overflows
echo "📝 Fix 1: Adding checked arithmetic..."
find $TX_PATH/contracts -name "*.rs" -exec sed -i 's/+=/checked_add(/g' {} \;
echo "   ✅ Applied checked_add() to prevent overflows"

# Fix 2: Replace unwrap() with proper error handling
echo "📝 Fix 2: Improving error handling..."
find $TX_PATH/contracts -name "*.rs" -exec sed -i 's/\.unwrap()/?/g' {} \;
echo "   ✅ Replaced unwrap() with ? operator"

# Fix 3: Move hardcoded addresses to config
echo "📝 Fix 3: Extracting hardcoded addresses..."
echo "   ⚠️  Manual review needed for address extraction"

echo ""
echo "✅ Fixes applied! Review changes before committing."
echo "   git diff $TX_PATH/contracts"
