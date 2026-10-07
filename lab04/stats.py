def parse_record(line: str) -> dict:
    city, temp, date = parts
    city = city.strip()
    date = date.strip()

    if not city:
        raise ValueError(f"empty city in line: {line!r}")
    if not date:
        raise ValueError(f"empty date in line: {line!r}")

    try:
        temperature = float(temp)
    except ValueError as exc:
        raise ValueError(f"invalid temperature {temp!r} in line: {line!r}") from exc

    return {"city": city, "temperature": temperature, "date": date}

def read_valid(lines: list[str]) -> list[dict]
 """Parse journal lines."""
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records