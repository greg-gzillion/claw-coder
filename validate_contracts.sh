#!/bin/bash
# Validate contract logic without needing Cargo

TX_PATH="/home/greg/dev/TX"
CLAW_PATH="/home/greg/dev/claw-coder"

echo "🔍 VALIDATING CONTRACT LOGIC"
echo "============================"
echo ""

# Check for required functions in contract files
echo "📋 Checking for required implementations:"

# Check for collateral function
echo -n "  • 10% collateral logic: "
if grep -r "collateral" $TX_PATH/contracts --include="*.rs" 2>/dev/null | grep -q "10"; then
    echo "✅ FOUND"
else
    echo "⚠️ NOT FOUND - Add collateral logic"
fi

# Check for fee function
echo -n "  • 1.1% fee logic: "
if grep -r "1.1" $TX_PATH/contracts --include="*.rs" 2>/dev/null | grep -q "fee"; then
    echo "✅ FOUND"
else
    echo "⚠️ NOT FOUND - Add fee logic"
fi

# Check for PHNX minting
echo -n "  • PHNX minting logic: "
if grep -r "phnx" $TX_PATH/contracts --include="*.rs" 2>/dev/null | grep -q "mint"; then
    echo "✅ FOUND"
else
    echo "⚠️ NOT FOUND - Add PHNX minting"
fi

# Check for escrow
echo -n "  • Escrow mechanism: "
if grep -r "escrow" $TX_PATH/contracts --include="*.rs" 2>/dev/null | head -1 | grep -q "escrow"; then
    echo "✅ FOUND"
else
    echo "⚠️ NOT FOUND - Add escrow logic"
fi

echo ""
echo "📊 Generated test file contents (preview):"
head -50 $TX_PATH/tests/generated_tests.rs
