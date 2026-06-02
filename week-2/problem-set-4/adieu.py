def main():
    text = adieu()
    print(text)

name_list = []

def adieu():
    while True:
        try:
            name = input("Name: \n").strip()
            name_list.append(name)
            continue
        except EOFError:
            return lyric(name_list)

def lyric(list):
    if len(list) == 1:
        return (f"Adieu, adieu, to {list[0]}")
    elif len(list) == 2:
        return (f"Adieu, adieu, to {list[0]} and {list[1]}")
    else:
        greet = "Adieu, adieu, to"
        edit_list = list[:-1]
        for i in edit_list:
            greet = greet + " " + i + ","
        greet = greet + " and " + list[-1]
        return greet

main()
