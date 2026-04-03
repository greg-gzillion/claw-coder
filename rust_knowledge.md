# Rust Standard Library Knowledge Base

## Core Types
- `Option<T>`: Represents optional values (Some/None)
- `Result<T, E>`: Error handling (Ok/Err)
- `Vec<T>`: Growable array type
- `String`: UTF-8 encoded string
- `HashMap<K, V>`: Hash map collection

## Key Traits
- `Clone`: Types that can be duplicated
- `Copy`: Types that can be copied implicitly
- `Debug`: Formatter for debugging
- `Display`: Formatter for user output
- `Default`: Types with default values
- `Iterator`: Types that produce sequences

## Smart Pointers
- `Box<T>`: Heap allocation
- `Rc<T>`: Reference counting (single-threaded)
- `Arc<T>`: Atomic reference counting (multi-threaded)
- `RefCell<T>`: Interior mutability

## Concurrency
- `std::thread`: Native threads
- `std::sync`: Synchronization primitives (Mutex, RwLock)
- `std::mpsc`: Multi-producer, single-consumer channels
- `async/await`: Asynchronous programming

## Common Patterns
- Builder pattern for complex construction
- RAII for resource management
- Error handling with `?` operator
- Iterators for collection processing
