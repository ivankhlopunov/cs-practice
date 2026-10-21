from pathlib import Path
import os

paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    
    for path in paths:
        name = path.split("/")[-1]
        extension = name.rsplit(".", 1)[-1] if "." in name else ""
        
        counts[extension] = counts.get(extension, 0) + 1
     
    return counts