from logstats import count_levels, top_errors, format_report

path = input().strip()

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

total = counts["DEBUG"] + counts["ERROR"] + counts["INFO"] + counts["WARNING"]

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