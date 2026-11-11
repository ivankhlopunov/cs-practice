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