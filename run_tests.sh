#!/bin/bash
# Run tests against actual contract directories

TX_PATH="/home/greg/dev/TX"
CLAW_PATH="/home/greg/dev/claw-coder"

echo "🧪 RUNNING TESTS AGAINST CONTRACTS"
echo "=================================="
echo ""

# Find all contract directories that have Cargo.toml
echo "📁 Finding contract directories..."
CONTRACT_DIRS=$(find $TX_PATH/contracts -name "Cargo.toml" -type f -exec dirname {} \; 2>/dev/null)

if [ -z "$CONTRACT_DIRS" ]; then
    echo "⚠️ No Cargo.toml files found in contracts directory"
    echo ""
    echo "📋 Your generated test file is at: $TX_PATH/tests/generated_tests.rs"
    echo ""
    echo "To use these tests, you can:"
    echo "  1. Copy them to an existing test directory:"
    echo "     cp $TX_PATH/tests/generated_tests.rs /path/to/contract/tests/"
    echo ""
    echo "  2. Or run as a standalone script (no compilation needed for review):"
    echo "     cat $TX_PATH/tests/generated_tests.rs"
    echo ""
    echo "  3. The tests validate:"
    echo "     - BTC/ETH/XRP to TESTUSD conversion"
    echo "     - 10% collateral locking"
    echo "     - 1 PHNX per $1 TESTUSD minting"
    echo "     - 66.7% governance pass threshold"
else
    echo "✅ Found contract directories with Cargo.toml:"
    echo "$CONTRACT_DIRS" | head -5
    echo ""
    
    # Run tests in each contract directory
    for dir in $(echo "$CONTRACT_DIRS" | head -3); do
        echo "📦 Testing in: $dir"
        cd $dir
        cargo test --lib 2>/dev/null | head -10 || echo "   No tests found"
        echo ""
    done
fi

echo ""
echo "💡 To integrate generated tests into your contracts:"
echo "   cp $TX_PATH/tests/generated_tests.rs /home/greg/dev/TX/contracts/phoenix_auction/tests/"
