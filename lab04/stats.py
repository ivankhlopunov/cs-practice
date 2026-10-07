def parse_record(line: str) -> dict:
    fields = line.split(";")
    if len(fields) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(fields)}")

    city, temperature_str, date = fields
    city = city.strip()
    temperature_str = temperature_str.strip()
    date = date.strip()

    if not city:
        raise ValueError("пустое название города")
    if not date:
        raise ValueError("пустая дата")

    try:
        temperature_str = float(temperature_str)
    except ValueError:
        raise ValueError(f"температура '{temperature_str}' — не число")

    return {"city": city, "temperature_str": temperature, "date": date}


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


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0) + r["temperature"]
        counts[city] = counts.get(city, 0) + 1
    return {city: round(totals[city] / counts[city], 1) for city in totals}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""
    best = ""
    for city in sorted(averages):
        if best == "" or averages[city] > averages[best]:
            best = city
    return best