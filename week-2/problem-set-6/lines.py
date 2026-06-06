import sys

def loc(file):
    list = []
    blank = []
    comment = []
    for m in file:
        list.append(m)
        stripped = m.strip()
        if stripped == "":
            blank.append(m)
        elif stripped.startswith("#") == True:
            comment.append(m)
    return (len(list) - len(blank) - len(comment))

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")
    elif sys.argv[1][-3:] == ".py":
        try:
            with open(sys.argv[1], "r") as file:
                print(loc(file))
        except FileNotFoundError:
            sys.exit("File does not exist")
