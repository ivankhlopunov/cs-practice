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
    counts = {}
    for line in lines:
        if not line.strip():
            continue

        parts = line.strip().split(maxsplit=2)

        if len(parts) < 3:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue

        time, level, message = parts

        if level not in LEVELS:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        else:
            counts[level] = counts.get(level, 0) + 1

    return counts

def top_errors(lines: list[str], n: int) -> dict:
    errors = {}
    for line in lines:
        if not line.strip():
            continue

        parts = line.strip().split(maxsplit=2)

        if len(parts) < 3:
            continue

        time, level, message = parts

        if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
            continue

        if level == "ERROR":
            errors[message] = errors.get(message, 0) + 1

    result = []

    for message, count in errors.items():
        result.append([message, count])

    return result[:n]

def format_report(counts: dict, errors: list[list]) -> str:
    report = "Отчёт по журналу\n\n"
    for level, count in sorted(counts.items()):
        report += level + ": " + str(count) + "\n"

    report += "\nЧастые ошибки:\n"

    for message, count in errors:
        report += "- " + message + " — " + str(count) + "\n"

    return report