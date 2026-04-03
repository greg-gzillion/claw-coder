# Rust Patterns for TX Blockchain

## Smart Contract Patterns
- **Ownership pattern**: Use `owner` field with authorization checks
- **Escrow pattern**: Two-party locking with release conditions
- **Factory pattern**: Create multiple instances from one contract

## Error Handling in CosmWasm
- Use `ContractError` enum with proper error types
- Implement `From` traits for external errors
- Use `ensure!()` macro for precondition checks

## Storage Patterns
- `Item` for single values
- `Map` for key-value pairs
- `IndexedMap` for secondary indexes
- `SnapshotMap` for historical values

## Testing Patterns
- Unit tests with `#[cfg(test)]`
- Integration tests with `multi_test` crate
- Property-based tests with `proptest`
