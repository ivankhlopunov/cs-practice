def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()
    
    captions = lines[0].strip(",")
    records = []
    
    for line in lines[1:]:
        values = line.split(",")
        record = {}
        
        for key, value in zip(captions, values):
            record[key.strip()] = value.strip()
            
        records.append(record)
        
    return records


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_key = ""
    
    for line in lines:
        line = line.split("#")[0].strip()
        
        if not line:
            continue
        
        if line.split()[0] == "-":
            settings[current_key].append(line[2:])
        else:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            
            if not value == "":
                settings[key] = []
            elif value.isdigit():
                settings[key] = int(value)
            elif value.replace(".", "", 1).replace(".", "", 1).isdigit():
                settings[key] = float(value.replace(",", "."))
            elif value.lower() in ("true", "yes"):
                settings[key] = True
            elif value.lower() in ("false", "no"):
                settings[key] = False
            else:
                settings[key] = value
                
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = id) -> list[dict]:
    result = []
    
    for row in rows:
        new_row = extra.get(row.get(key), {}).copy()
        new_row.update(row)
        result.append(new_row)
        
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)