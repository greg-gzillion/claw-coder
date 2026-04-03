# Rust + WebAssembly Knowledge Base
*Essential for CosmWasm smart contracts and blockchain development*

## Core Concepts

### Why Rust + WASM?
- **Performance**: Near-native speed in the browser/blockchain
- **Safety**: Rust's memory safety guarantees
- **Portability**: Runs anywhere WebAssembly runs (Cosmos, Ethereum, browsers)
- **Tooling**: Excellent compiler toolchain (wasm-pack, wasm-bindgen)

### Key Tools
- `wasm-pack`: Build Rust-generated WebAssembly packages
- `wasm-bindgen`: Facilitates high-level interactions between Rust and JavaScript
- `wasm32-unknown-unknown`: Rust compilation target for WebAssembly
- `wasm32-wasi`: WebAssembly System Interface for non-browser environments

### Common Patterns

#### 1. Exporting Rust Functions to JavaScript
```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}
```

## CosmWasm Connection

CosmWasm smart contracts compile Rust to WebAssembly, making this book directly relevant:
- **Entry Points** become exported WASM functions
- **Storage** uses WASM linear memory
- **Message Passing** uses WASM host functions
- **Gas Metering** is implemented in the WASM runtime

## Optimization Tips

### Binary Size
```toml
# In Cargo.toml
[profile.release]
opt-level = "z"      # Optimize for size
lto = true          # Link-time optimization
codegen-units = 1   # Better optimization
```
