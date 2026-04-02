#!/usr/bin/env python3
"""
Claw-Coder - Dual-Source Blockchain Development Agent
Ensures TX project conforms to TXdocumentation standards
"""

import os
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime
from difflib import SequenceMatcher

class ClawCoder:
    def __init__(self):
        # Two critical paths
        self.docs_path = Path("/home/greg/dev/TXdocumentation")
        self.project_path = Path("/home/greg/dev/TX")
        self.agent_path = Path("/home/greg/dev/claw-coder")
        
        # Storage for cross-referenced knowledge
        self.docs_knowledge = {}  # What the docs say
        self.project_knowledge = {}  # What the code does
        self.compliance_report = {}  # Where they diverge
        
        # Learning data
        self.scan_file = self.agent_path / ".claw_coder_scan.json"
        self.learning_file = self.agent_path / ".claw_coder_learning.json"
        
        # Initialize
        self._load_or_scan()
        self._cross_reference()
        self._generate_compliance_report()
    
    def _load_or_scan(self):
        """Load previous scan or perform fresh scan of both repos"""
        if self.scan_file.exists():
            try:
                with open(self.scan_file, 'r') as f:
                    data = json.load(f)
                    self.docs_knowledge = data.get('docs_knowledge', {})
                    self.project_knowledge = data.get('project_knowledge', {})
                    print(f"📚 Loaded scan from {data.get('last_scan', 'unknown')}")
                    print(f"   Docs: {len(self.docs_knowledge.get('files', []))} files")
                    print(f"   Project: {len(self.project_knowledge.get('files', []))} files")
                    return
            except:
                pass
        
        self._scan_both_repos()
    
    def _scan_both_repos(self):
        """Scan both TXdocumentation and TX project"""
        print("\n🔍 FIRST-TIME SCAN - Building knowledge base...")
        print("=" * 60)
        
        # Scan documentation
        print("\n📖 Scanning TXdocumentation (source of truth)...")
        self.docs_knowledge = self._scan_directory(self.docs_path, 'docs')
        
        # Scan project
        print("\n💻 Scanning TX project (your implementation)...")
        self.project_knowledge = self._scan_directory(self.project_path, 'project')
        
        # Save scan
        scan_data = {
            'docs_knowledge': self.docs_knowledge,
            'project_knowledge': self.project_knowledge,
            'last_scan': datetime.now().isoformat()
        }
        
        with open(self.scan_file, 'w') as f:
            json.dump(scan_data, f, indent=2)
        
        print(f"\n✅ Scan complete!")
        print(f"   📖 TXdocumentation: {len(self.docs_knowledge.get('files', []))} files")
        print(f"   💻 TX Project: {len(self.project_knowledge.get('files', []))} files")
    
    def _scan_directory(self, path, source_type):
        """Scan a directory and extract structured knowledge"""
        knowledge = {
            'files': [],
            'smart_tokens': [],
            'smart_contracts': [],
            'dex_info': [],
            'validator_info': [],
            'fee_model': [],
            'api_endpoints': [],
            'code_examples': [],
            'requirements': []
        }
        
        if not path.exists():
            print(f"⚠️ Path not found: {path}")
            return knowledge
        
        for file_path in path.rglob("*"):
            if file_path.is_file() and not file_path.name.startswith('.'):
                rel_path = file_path.relative_to(path)
                
                # Skip binary files and common exclusions
                if file_path.suffix in ['.pyc', '.wasm', '.db', '.log']:
                    continue
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    file_info = {
                        'path': str(rel_path),
                        'size': file_path.stat().st_size,
                        'type': file_path.suffix,
                        'content_preview': content[:500]
                    }
                    
                    knowledge['files'].append(file_info)
                    
                    # Extract domain-specific knowledge
                    if source_type == 'docs':
                        self._extract_docs_knowledge(content, file_info, knowledge)
                    else:
                        self._extract_project_knowledge(content, file_info, knowledge)
                        
                except Exception as e:
                    continue
        
        return knowledge
    
    def _extract_docs_knowledge(self, content, file_info, knowledge):
        """Extract requirements from documentation"""
        content_lower = content.lower()
        
        # Smart token requirements
        if 'smart token' in content_lower or 'assetft' in content_lower:
            knowledge['smart_tokens'].append({
                'source': file_info['path'],
                'requirements': self._extract_requirements(content, ['must', 'should', 'required', 'feature'])
            })
        
        # Smart contract requirements
        if 'smart contract' in content_lower or 'cosmwasm' in content_lower:
            knowledge['smart_contracts'].append({
                'source': file_info['path'],
                'requirements': self._extract_requirements(content, ['entry_point', 'instantiate', 'execute', 'query'])
            })
        
        # DEX requirements
        if 'dex' in content_lower or 'order' in content_lower:
            knowledge['dex_info'].append({
                'source': file_info['path'],
                'requirements': self._extract_requirements(content, ['order', 'liquidity', 'pool'])
            })
        
        # Fee model
        if 'fee' in content_lower or 'gas' in content_lower:
            knowledge['fee_model'].append({
                'source': file_info['path'],
                'requirements': self._extract_requirements(content, ['fee', 'gas', 'cost'])
            })
    
    def _extract_project_knowledge(self, content, file_info, knowledge):
        """Extract implementation details from project"""
        content_lower = content.lower()
        
        # Smart token implementations
        if file_info['type'] == '.rs' and ('token' in content_lower or 'asset' in content_lower):
            knowledge['smart_tokens'].append({
                'source': file_info['path'],
                'implementations': self._extract_code_blocks(content)
            })
        
        # Smart contract implementations
        if file_info['type'] == '.rs' and ('contract' in content_lower or 'execute' in content_lower):
            knowledge['smart_contracts'].append({
                'source': file_info['path'],
                'implementations': self._extract_code_blocks(content)
            })
        
        # API/Endpoint implementations
        if file_info['type'] in ['.ts', '.tsx', '.js']:
            knowledge['api_endpoints'].append({
                'source': file_info['path'],
                'implementations': self._extract_code_blocks(content)
            })
    
    def _extract_requirements(self, content, keywords):
        """Extract requirement statements from text"""
        requirements = []
        lines = content.split('\n')
        
        for line in lines:
            line_lower = line.lower()
            if any(kw in line_lower for kw in keywords):
                if len(line.strip()) > 20:
                    requirements.append(line.strip())
        
        return requirements[:10]
    
    def _extract_code_blocks(self, content):
        """Extract code blocks from content"""
        code_blocks = re.findall(r'```(?:\w+)?\n(.*?)```', content, re.DOTALL)
        return [block[:200] for block in code_blocks[:5]]
    
    def _cross_reference(self):
        """Cross-reference docs requirements against project implementation"""
        print("\n🔄 Cross-referencing documentation vs implementation...")
        
        self.compliance_report = {
            'smart_tokens': self._check_compliance('smart_tokens'),
            'smart_contracts': self._check_compliance('smart_contracts'),
            'dex': self._check_compliance('dex_info'),
            'fee_model': self._check_compliance('fee_model')
        }
    
    def _check_compliance(self, category):
        """Check compliance for a specific category"""
        docs_items = self.docs_knowledge.get(category, [])
        project_items = self.project_knowledge.get(category, [])
        
        if not docs_items:
            return {'status': 'no_docs', 'message': 'No documentation found'}
        
        if not project_items:
            return {'status': 'missing', 'message': f'No implementation found for {category}'}
        
        # Simple compliance check - can be enhanced
        return {
            'status': 'partial',
            'docs_count': len(docs_items),
            'impl_count': len(project_items),
            'message': f'{len(project_items)} implementations for {len(docs_items)} documented requirements'
        }
    
    def _generate_compliance_report(self):
        """Generate detailed compliance report"""
        print("\n📋 COMPLIANCE REPORT")
        print("=" * 60)
        
        for category, report in self.compliance_report.items():
            status = report.get('status', 'unknown')
            status_icon = {
                'no_docs': '📭',
                'missing': '❌',
                'partial': '⚠️',
                'compliant': '✅'
            }.get(status, '❓')
            
            print(f"\n{status_icon} {category.upper()}")
            print(f"   {report.get('message', 'No info')}")
            
            if 'docs_count' in report:
                print(f"   Documentation requirements: {report['docs_count']}")
                print(f"   Implementations found: {report['impl_count']}")
    
    def search_docs(self, query):
        """Search documentation for relevant requirements"""
        query_lower = query.lower()
        results = []
        
        for file_info in self.docs_knowledge.get('files', []):
            if query_lower in file_info.get('content_preview', '').lower():
                results.append({
                    'file': file_info['path'],
                    'preview': file_info['content_preview'][:300]
                })
        
        return results[:5]
    
    def find_related_implementations(self, query):
        """Find project implementations related to documentation"""
        query_lower = query.lower()
        results = []
        
        for file_info in self.project_knowledge.get('files', []):
            if query_lower in file_info.get('content_preview', '').lower():
                results.append({
                    'file': file_info['path'],
                    'type': file_info['type']
                })
        
        return results[:5]
    
    def suggest_improvements(self):
        """Suggest improvements based on compliance gaps"""
        suggestions = []
        
        for category, report in self.compliance_report.items():
            if report.get('status') == 'missing':
                suggestions.append(f"Implement {category} based on documentation")
            elif report.get('status') == 'partial':
                suggestions.append(f"Review {category} implementations against documentation")
        
        return suggestions
    
    def generate_test_addresses(self):
        """Generate test addresses needed for auction system"""
        test_addresses = {
            'testnet': 'txchain-testnet-1',
            'rpc': 'https://rpc.testnet-1.coreum.dev:443',
            'tokens': {
                'TESTUSD': 'utestusd',
                'PHNX': 'uphnx',
                'TRUST': 'utrust',
                'DONT_TRUST': 'udonttrust'
            },
            'wallet_types': [
                'buyer_wallet',
                'seller_wallet',
                'escrow_wallet',
                'fee_collector_wallet',
                'validator_wallet'
            ]
        }
        
        print("\n🏦 TEST ADDRESSES NEEDED")
        print("=" * 40)
        print(f"Testnet: {test_addresses['testnet']}")
        print(f"RPC: {test_addresses['rpc']}")
        print("\nRequired Tokens:")
        for name, denom in test_addresses['tokens'].items():
            print(f"  • {name} ({denom})")
        print("\nRequired Wallets:")
        for wallet in test_addresses['wallet_types']:
            print(f"  • {wallet}")
        
        return test_addresses
    
    def interactive_mode(self):
        """Main interactive loop"""
        print("\n" + "=" * 70)
        print("🦞 Claw-Coder - Dual-Source Blockchain Agent")
        print("=" * 70)
        print("\nI understand TWO repos:")
        print("  📖 TXdocumentation - Source of truth (rules & standards)")
        print("  💻 TX Project - Your implementation")
        print("\nMy job: Ensure TX conforms to TXdocumentation")
        print("=" * 70)
        
        while True:
            try:
                print("\n📋 Commands:")
                print("  • compliance     - Show compliance report")
                print("  • search <term>  - Search documentation")
                print("  • find <term>    - Find related implementation")
                print("  • improve        - Get improvement suggestions")
                print("  • test-addresses - Show required test addresses")
                print("  • status         - Show scan statistics")
                print("  • help           - Show this help")
                print("  • exit           - Quit")
                
                user_input = input("\n🦞 You: ").strip().lower()
                
                if not user_input:
                    continue
                
                if user_input == 'exit':
                    print("\n👋 Keeping TX compliant with documentation!")
                    break
                
                elif user_input == 'compliance':
                    self._generate_compliance_report()
                
                elif user_input.startswith('search '):
                    query = user_input[7:]
                    results = self.search_docs(query)
                    if results:
                        print(f"\n📚 Found in documentation:")
                        for r in results:
                            print(f"\n  📄 {r['file']}")
                            print(f"  {r['preview'][:200]}...")
                    else:
                        print(f"\n❌ No documentation found for '{query}'")
                
                elif user_input.startswith('find '):
                    query = user_input[5:]
                    results = self.find_related_implementations(query)
                    if results:
                        print(f"\n💻 Found in project:")
                        for r in results:
                            print(f"  • {r['file']} ({r['type']})")
                    else:
                        print(f"\n❌ No implementation found for '{query}'")
                
                elif user_input == 'improve':
                    suggestions = self.suggest_improvements()
                    if suggestions:
                        print("\n💡 Improvement Suggestions:")
                        for s in suggestions:
                            print(f"  • {s}")
                    else:
                        print("\n✅ No immediate improvements needed!")
                
                elif user_input == 'test-addresses':
                    self.generate_test_addresses()
                
                elif user_input == 'status':
                    print(f"\n📊 Scan Status:")
                    print(f"  📖 Docs files: {len(self.docs_knowledge.get('files', []))}")
                    print(f"  💻 Project files: {len(self.project_knowledge.get('files', []))}")
                    print(f"  🏷️  Smart tokens doc: {len(self.docs_knowledge.get('smart_tokens', []))}")
                    print(f"  🔧 Smart tokens impl: {len(self.project_knowledge.get('smart_tokens', []))}")
                    print(f"  📜 Contracts doc: {len(self.docs_knowledge.get('smart_contracts', []))}")
                    print(f"  ⚙️ Contracts impl: {len(self.project_knowledge.get('smart_contracts', []))}")
                
                elif user_input == 'help':
                    continue
                
                else:
                    print("\n❌ Unknown command. Type 'help' for available commands.")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}")

def main():
    agent = ClawCoder()
    agent.interactive_mode()

if __name__ == "__main__":
    main()
