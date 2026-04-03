#!/bin/bash
# Master script to run all agents from correct locations

echo "🤖 RUNNING ALL CLAW-CODE AGENTS"
echo "================================"
echo ""

# Set paths
CLAW_PATH="/home/greg/dev/claw-coder"
TX_PATH="/home/greg/dev/TX"

# 1. Run auto-fix agent
echo "📦 1. Running Auto-Fix Agent..."
cd $CLAW_PATH
python3 auto_fix_agent.py
echo ""

# 2. Run test generator
echo "📦 2. Running Test Generator..."
cd $CLAW_PATH
python3 test_generator.py
echo ""

# 3. Run governance monitor
echo "📦 3. Running Governance Monitor..."
cd $CLAW_PATH
python3 governance_monitor.py
echo ""

# 4. Run optimization agent
echo "📦 4. Running Optimization Agent..."
cd $CLAW_PATH
python3 optimization_agent.py
echo ""

echo "✅ All agents complete!"
echo ""
echo "📁 Generated files locations:"
echo "   • Fixes: $CLAW_PATH/apply_fixes.sh"
echo "   • Tests: $TX_PATH/tests/generated_tests.rs"
echo "   • Governance: $TX_PATH/governance_report.json"
echo "   • Optimizations: $TX_PATH/optimization_report.json"
