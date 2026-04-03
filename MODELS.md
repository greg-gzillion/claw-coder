# Model Comparison Guide
=======================

## Which Model Should You Install?

### By Use Case:

| What You Do | Recommended Model | Size |
|-------------|-------------------|------|
| **Ask questions, chat, general help** | Llama 3.2 | 2GB |
| **Understand code, debug, explain** | Codellama 7B | 3.8GB |
| **Write code, generate functions** | DeepSeek Coder | 3.8GB |
| **Everything** | All 3 models | 9.6GB |
| **Limited disk space** | Llama 3.2 only | 2GB |

### Performance Comparison:

| Task | Llama 3.2 | Codellama | DeepSeek |
|------|-----------|-----------|----------|
| Chat speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Code explanation | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Code generation | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Memory usage | 2GB | 3.8GB | 3.8GB |
| Response time | 1-2 sec | 2-3 sec | 2-3 sec |

### Disk Space Requirements:

```
Minimal setup (Llama only):     2GB   (fast chat)
Code-only setup (2 models):     7.6GB (explain + generate)
Full setup (3 models):          9.6GB (everything)
```
