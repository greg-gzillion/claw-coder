#!/usr/bin/env python3
"""
Web Dashboard for PhoenixPME
- Real-time metrics display
- Historical charts
- Alert management
"""

from flask import Flask, render_template_string, jsonify
import subprocess
import json
from datetime import datetime
from history_db import PhoenixPMEDatabase

app = Flask(__name__)
db = PhoenixPMEDatabase()

# HTML Template
DASHBOARD_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>PhoenixPME Dashboard</title>
    <style>
        body {
            font-family: monospace;
            background: #0a0a0a;
            color: #00ff00;
            margin: 0;
            padding: 20px;
        }
        .header {
            text-align: center;
            border-bottom: 2px solid #00ff00;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        .card {
            border: 1px solid #00ff00;
            padding: 15px;
            border-radius: 5px;
            background: #0a0a0a;
        }
        .card h3 {
            margin-top: 0;
            color: #00ff00;
        }
        .value {
            font-size: 2em;
            font-weight: bold;
        }
        .alert {
            border-color: #ff0000;
            color: #ff0000;
        }
        .alert .value {
            color: #ff0000;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #00ff00;
            padding: 8px;
            text-align: left;
        }
        th {
            background: #1a1a1a;
        }
        .refresh {
            text-align: center;
            margin-top: 20px;
            font-size: 0.8em;
        }
    </style>
    <script>
        function refreshData() {
            fetch('/api/metrics')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('crf_balance').innerText = '$' + data.crf_balance;
                    document.getElementById('phnx_supply').innerText = data.phnx_supply;
                    document.getElementById('fee_collected').innerText = '$' + data.fee_collected;
                    document.getElementById('active_escrows').innerText = data.active_escrows;
                });
        }
        setInterval(refreshData, 30000);
    </script>
</head>
<body>
    <div class="header">
        <h1>🦞 PhoenixPME Monitoring Dashboard</h1>
        <p>TX Blockchain - Precious Metals Exchange</p>
    </div>
    
    <div class="metrics">
        <div class="card">
            <h3>CRF Balance</h3>
            <div class="value" id="crf_balance">$--</div>
            <div>Community Reserve Fund</div>
        </div>
        
        <div class="card">
            <h3>PHNX Supply</h3>
            <div class="value" id="phnx_supply">--</div>
            <div>1 PHNX = $1 TESTUSD fees</div>
        </div>
        
        <div class="card">
            <h3>Total Fees Collected</h3>
            <div class="value" id="fee_collected">$--</div>
            <div>1.1% fee on all trades</div>
        </div>
        
        <div class="card">
            <h3>Active Escrows</h3>
            <div class="value" id="active_escrows">--</div>
            <div>10% collateral both parties</div>
        </div>
    </div>
    
    <div class="card">
        <h3>System Rules</h3>
        <table>
            <tr><th>Rule</th><th>Status</th><th>Current</th></tr>
            <tr><td>Collateral Requirement</td><td id="collateral_status">✅</td><td>10% both parties</td></tr>
            <tr><td>Fee Rate</td><td id="fee_status">✅</td><td>1.1%</td></tr>
            <tr><td>Inspection Window</td><td id="inspection_status">✅</td><td>48 hours</td></tr>
        </table>
    </div>
    
    <div class="refresh">
        <p>Auto-refreshes every 30 seconds | Last updated: <span id="timestamp">{{ timestamp }}</span></p>
    </div>
</body>
</html>
'''

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_HTML, timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/api/metrics')
def api_metrics():
    """API endpoint for metrics"""
    # Get status from shell script
    result = subprocess.run(['./status.sh'], capture_output=True, text=True, shell=True)
    
    # Parse metrics (simplified - would need proper parsing)
    metrics = {
        'crf_balance': 264.32,
        'phnx_supply': 247,
        'fee_collected': 2.91,
        'active_escrows': 12,
        'timestamp': datetime.now().isoformat()
    }
    
    return jsonify(metrics)

@app.route('/api/history')
def api_history():
    """Get historical data"""
    trends = db.get_trends(days=30)
    return jsonify([{'timestamp': t[0], 'crf': t[1], 'phnx': t[2]} for t in trends])

if __name__ == '__main__':
    print("🦞 PhoenixPME Dashboard starting...")
    print("📍 Open http://localhost:5000 in your browser")
    app.run(host='0.0.0.0', port=5000, debug=False)
