def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and prefix(s) == True and format(s) == True and zero(s) == True and detail(s) == True:
        return True
    else:
        return False

def prefix(m):
    if m[0].isalpha() == True and m[1].isalpha() == True:
        return True
    else:
        return False

def format(h):
    index_char = []
    index_num = []

    for i in h:
        if i.isnumeric() == True:
            index_num.append(h.index(i))
        elif i.isalpha() == True:
            index_char.append(h.index(i))

    if index_num != []:
        if min(index_num) < max(index_char) < max(index_num):
            return False
        else:
            return True
    else:
        return True


def zero(k):
    num = []
    for i in k:
        if i.isnumeric() == True:
            num.append(i)

    if "0" in num and num.index("0") == 0:
        return False
    else:
        return True

def detail(text):
    for i in text:
        if i in [".", ",", "?", ";", "'", ":", "(", ")", "!", '"', "-", "_", "/", "{", "@", "[", "]", "*", " "]:
            return False
    return True

main()
