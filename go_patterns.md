# Go Patterns for TX Blockchain

## Concurrency Patterns
- **Goroutines**: Lightweight threads
- **Channels**: Communicate between goroutines
- **Select**: Wait on multiple channel operations
- **Worker pools**: Control concurrent execution

## Error Handling
- Return errors as last value
- Use `%w` for error wrapping
- Custom error types with `errors.Is()`

## Blockchain-Specific
- `sync.RWMutex` for shared state
- Context for timeout/cancellation
- Atomic operations for counters
