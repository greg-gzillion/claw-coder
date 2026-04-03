# 🦞 Claw-Coder Reference Manual
## Intelligent Assistant for PhoenixPME on TX Blockchain

**Version:** 1.0
**Last Updated:** April 2, 2026
**Location:** `/home/greg/dev/claw-coder/`
**Project:** PhoenixPME Auction System on TX Blockchain

---

## 🚀 Quick Start

```bash
# Navigate to agent directory
cd /home/greg/dev/claw-coder

# Run everything (complete system check)
./run_all_agents.sh

# Check current status
./status.sh

# Validate contracts against documentation
./validate_contracts.sh
```

## 🤖 Core Agent Commands

```bash
# Run all agents
cd /home/greg/dev/claw-coder && ./run_all_agents.sh

# Auto-Fix Agent (bug detection)
python3 auto_fix_agent.py

# Test Generator
python3 test_generator.py

# Governance Monitor
python3 governance_monitor.py

# Optimization Agent
python3 optimization_agent.py
```

## 🔍 Analysis & Validation

```bash
# Validate contract logic
./validate_contracts.sh

# Deep analysis (docs vs code)
python3 deep_analysis_agent.py

# Enhanced analysis
python3 enhanced_analysis_agent.py

# Multi-currency gateway
python3 multi_currency_payment.py

# Market data integration
python3 market_data_integration.py
```

## 💻 Code Generation

```bash
# Build PHNX token contract
cd /home/greg/dev/TX/contracts/phoenix_governance && cargo build

# Generate auction engine
python3 phoenix_accurate_engine.py

# Generate multi-currency gateway
python3 implement_multi_currency.py

# Generate governance system
python3 implement_governance.py
```

## 🧪 Testing

```bash
# Run generated tests
cd /home/greg/dev/TX && cargo test --test generated_tests

# Run PHNX contract tests
cd /home/greg/dev/TX/contracts/phoenix_governance && cargo test

# Run specific test
cargo test test_btc_conversion -- --nocapture

# Test runner (no Cargo)
./run_tests.sh
```

## 📊 Governance & Monitoring

```bash
# Monitor CRF and PHNX
python3 governance_monitor.py

# Check CRF balance
cat /home/greg/dev/TX/governance_report.json | jq '.crf_balance'

# View PHNX distribution
cat /home/greg/dev/TX/governance_report.json | jq '.phnx_distribution'

# Track active proposals
cat /home/greg/dev/TX/governance_report.json | jq '.proposals[] | {id, title, status}'
```

## ⚡ Optimization

```bash
# Run optimization scan
python3 optimization_agent.py

# View HIGH priority optimizations
cat /home/greg/dev/TX/optimization_report.json | jq '.[] | select(.gas_savings=="HIGH")'

# Count optimizations by type
cat /home/greg/dev/TX/optimization_report.json | jq 'group_by(.issue) | map({issue: .[0].issue, count: length})'
```

## 🔧 Auto-Fix & Repair

```bash
# Apply auto-generated fixes
./apply_fixes.sh

# Review changes before committing
git diff /home/greg/dev/TX/contracts --stat

# View fix details
cat apply_fixes.sh
```

## 📁 File Locations

| File | Path | Purpose |
|------|------|---------|
| `run_all_agents.sh` | `/home/greg/dev/claw-coder/` | Run all agents |
| `status.sh` | `/home/greg/dev/claw-coder/` | Check system status |
| `validate_contracts.sh` | `/home/greg/dev/claw-coder/` | Validate contract logic |
| `apply_fixes.sh` | `/home/greg/dev/claw-coder/` | Apply auto-fixes |
| `generated_tests.rs` | `/home/greg/dev/TX/tests/` | Generated test suite |
| `governance_report.json` | `/home/greg/dev/TX/` | CRF & PHNX data |
| `optimization_report.json` | `/home/greg/dev/TX/` | Gas optimization findings |
| `phnx.rs` | `/home/greg/dev/TX/contracts/phoenix_governance/src/` | PHNX token |

## 🔧 Troubleshooting

### CLI Locked Up
```bash
pkill -f cat
pkill -f python3
```

### Tests Not Running
```bash
# Check if test file exists
ls -la /home/greg/dev/TX/tests/generated_tests.rs

# Regenerate tests
python3 test_generator.py
```

### PHNX Not Detected
```bash
# Rebuild PHNX contract
cd /home/greg/dev/TX/contracts/phoenix_governance && cargo build

# Run validation again
cd /home/greg/dev/claw-coder && ./validate_contracts.sh
```
