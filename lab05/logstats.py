from collections import defaultdict

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line: str) -> dict:
    if line is None:
        raise ValueError("Пустая строка")
    stripped = line.strip()
    if not stripped:
        raise ValueError("Пустая строка")
    parts = stripped.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Неправильное количество частей в строке")

    time, level, message = parts

    if level not in LEVELS:
        raise ValueError("Неизвестный уровень")

    return{"time": time, "level": level, "message": message}

def count_levels(lines: list[str]) -> dict:
    parts = line.strip().split(maxsplit=2)
    if not is_valid_event(line):
        raise ValueError("Некорректная строка")

    time, level, message = parts

    return{"time": time, "level": level, "message": message}