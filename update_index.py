import os
import json
from pathlib import Path

INDEX_FILE = Path.home() / ".claw_index.json"

# Load existing index
if INDEX_FILE.exists():
    with open(INDEX_FILE, 'r') as f:
        index = json.load(f)
else:
    index = {"files": {}, "docs": {}, "last_scan": None}

# Index TXdocumentation (all files)
docs_path = Path("/home/greg/dev/TXdocumentation")
doc_count = 0
file_types = {}

if docs_path.exists():
    print("📚 Indexing TXdocumentation...")
    for filepath in docs_path.rglob("*"):
        if filepath.is_file() and filepath.stat().st_size < 500000:  # 500KB max
            ext = filepath.suffix.lower()
            file_types[ext] = file_types.get(ext, 0) + 1
            
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    lines = len(content.split('\n'))
                    index["docs"][str(filepath)] = {
                        "type": "doc",
                        "lines": lines,
                        "size": len(content),
                        "ext": ext,
                        "modified": str(filepath.stat().st_mtime)
                    }
                    doc_count += 1
                    if doc_count % 100 == 0:
                        print(f"  Indexed {doc_count} docs...")
            except Exception as e:
                pass

# Update stats
index["stats"] = {
    "code_files": len(index.get("files", {})),
    "doc_files": len(index.get("docs", {})),
    "total_lines": sum(f.get("lines", 0) for f in index.get("files", {}).values()) + 
                  sum(d.get("lines", 0) for d in index.get("docs", {}).values()),
    "paths": ["/home/greg/dev/TX", "/home/greg/dev/TXdocumentation"]
}
index["last_scan"] = "2026-04-02T22:30:00"

# Save
with open(INDEX_FILE, 'w') as f:
    json.dump(index, f, indent=2)

print(f"\n✅ Indexing complete!")
print(f"   📁 Docs indexed: {doc_count}")
print(f"   📊 File types found: {dict(list(file_types.items())[:10])}")
print(f"   📚 Total docs: {index['stats']['doc_files']}")
