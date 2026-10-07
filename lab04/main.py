import sys
from stats import parse_record, average_by_city, read_valid, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)

    empty_count = sum(1 for line in lines if line.strip() == "")
    error_count = len(lines) - empty_count - len(records)

    print(len(records))
    print(error_count)

    if records:
        averages = average_by_city(records)
        city = warmest_city(records)
        print(f"{averages[city]:.1f}")
    else:
        print("0.0")


if __name__ == "__main__":
    main()