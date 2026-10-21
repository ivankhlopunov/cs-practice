from logstats import parse_event, top_errors, format_report

path = input().strip()

counts = {"DEBUG": 0, "ERROR": 0, "INFO": 0, "WARNING": 0, "BROKEN": 0}

with open(path, encoding="utf-8") as log:
    for line in log:
        parts = line.strip().split(maxsplit=2)

        if len(parts) < 3:
            counts["BROKEN"] += 1
        else:
            time, level, message = parts

            if level not in counts or level == "BROKEN":
                counts["BROKEN"] += 1
            else:
                event = parse_event(line)
                counts[event["level"]] += 1

total = (counts["DEBUG"] + counts["ERROR"] + counts["INFO"] + counts["WARNING"])

error_count = counts["ERROR"]
broken_count = counts["BROKEN"]

print(total)
print(error_count)
print(broken_count)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

report = format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(report)