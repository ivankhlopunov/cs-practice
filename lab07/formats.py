def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().split("\n")
    captions = lines[0].strip(",")
    
    records = []
    
    for line in lines[1:]:
        values = line.split(",")
        record = {}
        
        for i in range(len(captions)):
            record[captions[i]] = values[i]
            
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
            
            if value == "":
                settings[key] = []
            elif value.isdigit():
                settings[key] = int(value)
            elif value.replace(".", "", 1).isdigit():
                settings[key] = float(value)
            elif value == "true" or value == "yes":
                settings[key] = True
            elif value == "false" or value == "no":
                settings[key] = False
            else:
                settings[key] = value
                
    return settings
