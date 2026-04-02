#!/usr/bin/env python3
"""
Deep Analysis Agent - Examines TX project and TXdocumentation
Makes intelligent suggestions based on actual code and documentation
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class DeepAnalysisAgent:
    def __init__(self):
        self.tx_project = Path("/home/greg/dev/TX")
        self.tx_docs = Path("/home/greg/dev/TXdocumentation")
        self.phoenix_docs = Path("/home/greg/dev/TX/docs") if Path("/home/greg/dev/TX/docs").exists() else None
        
        self.findings = {
            'implemented_features': [],
            'missing_features': [],
            'doc_vs_code_gaps': [],
            'suggestions': [],
            'critical_issues': [],
            'optimizations': []
        }
        
        self.doc_rules = {}
        self.code_features = {}
        
    def scan_project(self):
        """Deep scan of TX project"""
        print("\n🔍 SCANNING TX PROJECT")
        print("=" * 60)
        
        # Find all contract files
        contracts = list(self.tx_project.rglob("*.rs"))
        print(f"📄 Found {len(contracts)} Rust contracts")
        
        # Find all frontend components
        frontend = list(self.tx_project.rglob("*.tsx")) + list(self.tx_project.rglob("*.ts"))
        print(f"🎨 Found {len(frontend)} frontend files")
        
        # Find all scripts
        scripts = list(self.tx_project.rglob("*.sh"))
        print(f"🔧 Found {len(scripts)} shell scripts")
        
        # Analyze contract features
        for contract in contracts[:20]:  # Limit for performance
            try:
                content = contract.read_text()
                rel_path = contract.relative_to(self.tx_project)
                
                # Detect features
                if 'escrow' in content.lower():
                    self.code_features['escrow'] = self.code_features.get('escrow', []) + [str(rel_path)]
                if 'collateral' in content.lower():
                    self.code_features['collateral'] = self.code_features.get('collateral', []) + [str(rel_path)]
                if 'fee' in content.lower():
                    self.code_features['fee'] = self.code_features.get('fee', []) + [str(rel_path)]
                if 'auction' in content.lower():
                    self.code_features['auction'] = self.code_features.get('auction', []) + [str(rel_path)]
                if 'trust' in content.lower() or 'reputation' in content.lower():
                    self.code_features['reputation'] = self.code_features.get('reputation', []) + [str(rel_path)]
                if 'phnx' in content.lower() or 'governance' in content.lower():
                    self.code_features['governance'] = self.code_features.get('governance', []) + [str(rel_path)]
                    
            except Exception as e:
                continue
        
        return self.code_features
    
    def scan_documentation(self):
        """Scan both TXdocumentation and Phoenix docs"""
        print("\n📖 SCANNING DOCUMENTATION")
        print("=" * 60)
        
        # Scan TXdocumentation
        tx_doc_files = list(self.tx_docs.rglob("*.md"))
        print(f"📚 TXdocumentation: {len(tx_doc_files)} files")
        
        # Extract rules from TX docs
        for doc in tx_doc_files[:50]:  # Limit for performance
            try:
                content = doc.read_text()
                
                # Look for requirements
                if 'must' in content.lower() or 'required' in content.lower():
                    sentences = re.findall(r'[^.!?]*(?:must|required|shall)[^.!?]*[.!?]', content.lower())
                    for sent in sentences[:3]:
                        self.doc_rules['tx_requirements'] = self.doc_rules.get('tx_requirements', []) + [sent.strip()]
                        
            except Exception as e:
                continue
        
        # Scan Phoenix docs if exists
        if self.phoenix_docs and self.phoenix_docs.exists():
            phoenix_files = list(self.phoenix_docs.rglob("*.md"))
            print(f"🏛️ Phoenix docs: {len(phoenix_files)} files")
            
            for doc in phoenix_files:
                try:
                    content = doc.read_text()
                    rel_path = doc.relative_to(self.phoenix_docs)
                    
                    # Extract specs
                    if 'auction' in content.lower():
                        self.doc_rules['phoenix_auction'] = self.doc_rules.get('phoenix_auction', []) + [str(rel_path)]
                    if 'fee' in content.lower():
                        self.doc_rules['phoenix_fee'] = self.doc_rules.get('phoenix_fee', []) + [str(rel_path)]
                        
                except Exception as e:
                    continue
        
        return self.doc_rules
    
    def analyze_gaps(self):
        """Compare documentation requirements against actual code"""
        print("\n🔬 ANALYZING GAPS BETWEEN DOCS AND CODE")
        print("=" * 60)
        
        # Required features from your README
        required_features = {
            '10% collateral from both parties': 'collateral',
            '1.1% fee': 'fee',
            '48-hour inspection': 'inspection',
            'PHNX governance tokens': 'governance',
            'TRUST reputation tokens': 'reputation',
            'DONT_TRUST reputation tokens': 'reputation',
            'Community Reserve Fund': 'crf',
            'Multi-wallet support': 'wallet',
            'TESTUSD settlement': 'settlement'
        }
        
        for feature, category in required_features.items():
            if category in self.code_features:
                self.findings['implemented_features'].append(feature)
            else:
                self.findings['missing_features'].append(feature)
        
        # Check for multi-currency support (from your latest request)
        multi_currency_code = False
        for file in self.tx_project.rglob("*"):
            if file.is_file():
                try:
                    content = file.read_text()
                    if any(currency in content.lower() for currency in ['btc', 'eth', 'xrp', 'currency']):
                        multi_currency_code = True
                        break
                except:
                    continue
        
        if not multi_currency_code:
            self.findings['suggestions'].append({
                'priority': 'HIGH',
                'category': 'Multi-Currency Payments',
                'suggestion': 'Implement payment gateway for BTC, ETH, XRP with instant TESTUSD conversion',
                'reason': 'Users need flexibility to deposit in their preferred cryptocurrency',
                'effort': 'Medium',
                'impact': 'High'
            })
        
        # Check for price oracle
        oracle_exists = False
        for file in self.tx_project.rglob("*"):
            if file.is_file():
                try:
                    content = file.read_text()
                    if 'oracle' in content.lower() or 'price' in content.lower():
                        oracle_exists = True
                        break
                except:
                    continue
        
        if not oracle_exists:
            self.findings['suggestions'].append({
                'priority': 'HIGH',
                'category': 'Price Oracle',
                'suggestion': 'Integrate Chainlink or Pyth oracles for real-time BTC/ETH/XRP prices',
                'reason': 'Need accurate conversion rates for multi-currency deposits',
                'effort': 'High',
                'impact': 'High'
            })
        
        return self.findings
    
    def generate_suggestions(self):
        """Generate actionable suggestions"""
        print("\n💡 GENERATING INTELLIGENT SUGGESTIONS")
        print("=" * 60)
        
        # Suggestion 1: Multi-currency gateway
        self.findings['suggestions'].append({
            'priority': 'HIGH',
            'category': 'Multi-Currency',
            'suggestion': 'Create payment gateway that accepts BTC/ETH/XRP on testnet',
            'implementation': '''
            def deposit_collateral(currency, amount):
                # 1. Get exchange rate from oracle
                rate = oracle.get_price(currency)
                # 2. Convert to USD
                usd_value = amount * rate
                # 3. Convert to TESTUSD
                testusd_amount = usd_value * 1_000_000
                # 4. Lock collateral
                lock_collateral(testusd_amount)
            ''',
            'benefit': 'Users can deposit in any currency, all settle in TESTUSD'
        })
        
        # Suggestion 2: Automated settlement
        if '48-hour inspection' in self.findings['missing_features']:
            self.findings['suggestions'].append({
                'priority': 'MEDIUM',
                'category': 'Settlement',
                'suggestion': 'Implement automated 48-hour inspection timer',
                'implementation': '''
                # After auction completion
                inspection_deadline = block.timestamp + 48 * 3600
                # If no dispute by deadline, auto-release funds
                ''',
                'benefit': 'Reduces need for manual intervention'
            })
        
        # Suggestion 3: PHNX governance UI
        self.findings['suggestions'].append({
            'priority': 'MEDIUM',
            'category': 'Governance',
            'suggestion': 'Create governance dashboard for PHNX holders',
            'implementation': 'Frontend component showing proposals, voting power, CRF balance',
            'benefit': 'Transparent community governance'
        })
        
        # Suggestion 4: Test automation
        self.findings['suggestions'].append({
            'priority': 'LOW',
            'category': 'Testing',
            'suggestion': 'Add integration tests for multi-currency deposits',
            'implementation': 'Test BTC, ETH, XRP deposits on testnet',
            'benefit': 'Ensures multi-currency works before mainnet'
        })
        
        return self.findings['suggestions']
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        
        print("\n" + "="*70)
        print("📊 DEEP ANALYSIS REPORT")
        print("="*70)
        
        # Summary
        print(f"\n✅ IMPLEMENTED FEATURES ({len(self.findings['implemented_features'])}):")
        for f in self.findings['implemented_features']:
            print(f"   • {f}")
        
        print(f"\n❌ MISSING FEATURES ({len(self.findings['missing_features'])}):")
        for f in self.findings['missing_features']:
            print(f"   • {f}")
        
        print(f"\n💡 SUGGESTIONS ({len(self.findings['suggestions'])}):")
        for s in self.findings['suggestions']:
            print(f"\n   [{s['priority']}] {s['category']}")
            print(f"   → {s['suggestion']}")
            print(f"   Benefit: {s['benefit']}")
        
        # Critical issues
        high_priority = [s for s in self.findings['suggestions'] if s['priority'] == 'HIGH']
        if high_priority:
            print(f"\n⚠️ CRITICAL ISSUES TO ADDRESS FIRST:")
            for s in high_priority:
                print(f"   • {s['suggestion']}")
        
        # Save report
        report = {
            'timestamp': datetime.now().isoformat(),
            'project_path': str(self.tx_project),
            'docs_path': str(self.tx_docs),
            'implemented_features': self.findings['implemented_features'],
            'missing_features': self.findings['missing_features'],
            'suggestions': self.findings['suggestions'],
            'code_features': list(self.code_features.keys()),
            'doc_coverage': len(self.doc_rules.keys())
        }
        
        report_file = self.tx_project / 'deep_analysis_report.json'
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n💾 Full report saved to: {report_file}")
        
        return report

def main():
    agent = DeepAnalysisAgent()
    
    print("\n" + "="*70)
    print("🤖 DEEP ANALYSIS AGENT - PhoenixPME")
    print("="*70)
    print("\nThis agent will:")
    print("   1. Scan your entire TX project")
    print("   2. Read all TXdocumentation")
    print("   3. Compare docs vs code")
    print("   4. Generate intelligent suggestions")
    
    # Run analysis
    agent.scan_project()
    agent.scan_documentation()
    agent.analyze_gaps()
    agent.generate_suggestions()
    agent.generate_report()
    
    print("\n✅ Analysis complete!")
    print("   Check deep_analysis_report.json for full details")

if __name__ == "__main__":
    main()
