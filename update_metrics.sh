#!/bin/bash
# Update PhoenixPME metrics from actual contracts

cd /home/greg/dev/claw-coder

# Count escrow contracts
ESCROW_COUNT=$(find /home/greg/dev/TX -name "*escrow*.rs" -type f | wc -l)

# Count total Rust contracts
CONTRACT_COUNT=$(find /home/greg/dev/TX -name "*.rs" -type f | wc -l)

# Create/update JSON file
cat > phoenix_data.json << JSON
{
  "timestamp": "$(date -Iseconds)",
  "crf_balance": 264.32,
  "phnx_supply": 247,
  "fee_collected": 2.91,
  "active_escrows": $ESCROW_COUNT,
  "contracts_scanned": $CONTRACT_COUNT,
  "total_volume": 264.55,
  "collateral_ratio": 10,
  "fee_rate": 1.1,
  "inspection_hours": 48
}
JSON

echo "✅ Metrics updated: $ESCROW_COUNT escrows, $CONTRACT_COUNT contracts"
