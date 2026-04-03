#!/bin/bash
# Launch all PhoenixPME monitoring systems

echo "🦞 Launching PhoenixPME Monitoring Suite"
echo "========================================"

# Start monitor daemon
echo "📊 Starting real-time monitor..."
python3 monitor_daemon.py &
MONITOR_PID=$!
echo "  Monitor PID: $MONITOR_PID"

# Start web dashboard
echo "🌐 Starting web dashboard..."
python3 dashboard.py &
DASHBOARD_PID=$!
echo "  Dashboard PID: $DASHBOARD_PID"
echo "  Dashboard URL: http://localhost:5000"

# Run initial AI fixer
echo "🤖 Running AI fixer..."
python3 ai_fixer.py

echo ""
echo "✅ All systems running!"
echo "  Monitor: kill $MONITOR_PID"
echo "  Dashboard: kill $DASHBOARD_PID"
echo ""
echo "Press Ctrl+C to stop all"

# Wait for interrupt
trap "kill $MONITOR_PID $DASHBOARD_PID; exit" INT
wait
