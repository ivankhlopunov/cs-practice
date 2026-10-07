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

def average_by_city(records: list[dict]) -> dict:
    """Calculates the average temperature"""
    totals = {}
    counts = {}
    for r in records:
        city = r["city"]
        totals[city] = totals.get(city, 0.0) + r["temp"]
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
    return averages

def warmest_city(records: list[dict]) -> str:
    """Returns the city with the highest temperature"""
    if not records:
        return ""

    averages = average_by_city(records)
    sorted_cities = sorted(averages.keys(), key=lambda c: (-averages[c], c))
    return sorted_cities[0]