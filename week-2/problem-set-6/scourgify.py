import sys
import csv


if len(sys.argv) in [1, 2]:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    if sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv":
        sys.exit("Not a CSV file")
    elif sys.argv[1][-4:] == ".csv" and sys.argv[2][-4:] == ".csv":
        try:
            with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w") as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({"first":first, "last":last, "house": row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
