#!/usr/bin/env python3
"""
Governance Monitor - Corrected paths
Location: /home/greg/dev/claw-coder/governance_monitor.py
"""

import json
from pathlib import Path
from datetime import datetime

# Correct paths
TX_PATH = Path("/home/greg/dev/TX")
CLAW_PATH = Path("/home/greg/dev/claw-coder")

class GovernanceMonitor:
    def __init__(self):
        self.crf_address = "testcore1m5adn3k68tk4zqmujpnstmp9r933jafzu44tnv"
        self.report_file = TX_PATH / "governance_report.json"
        
    def run(self):
        print("\n🏦 GOVERNANCE MONITOR")
        print("=" * 50)
        print(f"CRF Address: {self.crf_address}")
        print(f"Report saved to: {self.report_file}")
        
        # Load or create report
        if self.report_file.exists():
            with open(self.report_file, 'r') as f:
                report = json.load(f)
            print(f"\n📊 Last Report: {report.get('timestamp', 'Unknown')}")
            print(f"CRF Balance: ${report.get('crf_balance', 0) / 1_000_000:,.2f} TESTUSD")
        else:
            print("\n📊 No previous report found. Run simulation first.")
        
        return True

if __name__ == "__main__":
    monitor = GovernanceMonitor()
    monitor.run()
