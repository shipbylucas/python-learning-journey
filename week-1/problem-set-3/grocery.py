def main():
    grocery = gro_list()

def gro_list():
    gro_item = []
    while True:
        try:
            item = input()
            gro_item.append(item.upper())
            continue
        except EOFError:
            break
    return final(gro_item)

def final(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    unique.sort()
    for k in unique:
        if k != "":
            print (str(list.count(k)) + " " + k)

main()
