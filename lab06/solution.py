from pathlib import Path
import os

paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    
    for path in paths:
        name = path.split("/")[-1]
        extension = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        
        counts[extension] = counts.get(extension, 0) + 1
     
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    
    result = paths[0]
    
    for path in paths:
        if path.count("/") > result.count("/"):
            result = path
        elif path.count("/") == result.count("/") and path < result:
            result = path
            
    return result

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    i = 0
    
    while size >= 1024 and i < 4:
        size = size / 1024
        i += 1
        
    if i == 0:
        return str(n_bytes) + " Б"
    
    return "%.1f %s" % (size, units[i])