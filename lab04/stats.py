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
