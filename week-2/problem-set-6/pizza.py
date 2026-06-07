import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")
    elif sys.argv[1][-4:] == ".csv":
        try:
            file = open(sys.argv[1], "r")
            reader = csv.DictReader(file)
            if sys.argv[1] == "sicilian.csv":
                sipi = []
                for row in reader:
                    sipi.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
                print(tabulate(sipi, headers="keys", tablefmt="grid"))
            elif sys.argv[1] == "regular.csv":
                repi = []
                for row in reader:
                    repi.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
                print(tabulate(repi, headers="keys", tablefmt="grid"))
            file.close()
        except FileNotFoundError:
            sys.exit("File does not exit")
