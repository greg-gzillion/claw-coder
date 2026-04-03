#!/bin/bash
# Show status of all generated files
# Location: /home/greg/dev/claw-coder/status.sh

CLAW_PATH="/home/greg/dev/claw-coder"
TX_PATH="/home/greg/dev/TX"

echo "📊 CLAW-CODER STATUS REPORT"
echo "============================"
echo ""

echo "🔧 AGENT FILES:"
echo "   • Auto-fix: $CLAW_PATH/auto_fix_agent.py"
echo "   • Test gen: $CLAW_PATH/test_generator.py"
echo "   • Gov monitor: $CLAW_PATH/governance_monitor.py"
echo "   • Optimizer: $CLAW_PATH/optimization_agent.py"
echo ""

echo "📁 GENERATED OUTPUTS:"
[ -f "$CLAW_PATH/apply_fixes.sh" ] && echo "   ✅ apply_fixes.sh" || echo "   ❌ apply_fixes.sh"
[ -f "$TX_PATH/tests/generated_tests.rs" ] && echo "   ✅ generated_tests.rs" || echo "   ❌ generated_tests.rs"
[ -f "$TX_PATH/governance_report.json" ] && echo "   ✅ governance_report.json" || echo "   ❌ governance_report.json"
[ -f "$TX_PATH/optimization_report.json" ] && echo "   ✅ optimization_report.json" || echo "   ❌ optimization_report.json"
echo ""

echo "🚀 RUN COMMANDS:"
echo "   1. Run all agents:  ./run_all_agents.sh"
echo "   2. Apply fixes:     ./apply_fixes.sh"
echo "   3. Run tests:       ./run_tests.sh"
echo "   4. View status:     ./status.sh"
