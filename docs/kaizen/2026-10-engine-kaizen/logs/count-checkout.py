#!/usr/bin/env python3
"""Count repo file entries without following symlinks; preserve full checkout count."""
import json
import os
from pathlib import Path

root = Path(os.environ.get("SOCIAL_ENGINE_ROOT", ".")).resolve()
excluded_names = {".git", ".cache", ".venv", "venv", "node_modules", "__pycache__"}
total = symlinks = filtered = 0
for current, dirs, files in os.walk(root, followlinks=False):
    for name in dirs + files:
        path = Path(current) / name
        if path.is_dir() and not path.is_symlink():
            continue
        total += 1
        symlinks += int(path.is_symlink())
        if not any(part in excluded_names for part in path.relative_to(root).parts):
            filtered += 1
result = {
    "method": "os.walk(followlinks=False); count regular file entries and symlink entries; count .git/cache contents in total; omit named cache/dependency directories only in filtered count",
    "checkout_file_entries_including_git": total,
    "symlink_entries": symlinks,
    "excluded_named_cache_or_dependency_entries": total - filtered,
    "filtered_entries_excluding_named_cache_or_dependency_dirs": filtered,
    "excluded_directory_names": sorted(excluded_names),
}
print(json.dumps(result, indent=2))
