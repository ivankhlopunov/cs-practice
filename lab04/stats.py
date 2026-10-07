def parse_record(line: str) -> dict:
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(fields)}")

    city, temp_str, date = fields

    if not city:
        raise ValueError("пустое название города")
    if not date:
        raise ValueError("пустая дата")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"температура '{temp_str}' — не число")

    return {"city": city, "temp": temp, "date": date}

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            pass
    return records
    