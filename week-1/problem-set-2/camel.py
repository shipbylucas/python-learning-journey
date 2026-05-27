def main():
    camel = input("camelCase: ")
    print_snake(camel)

def print_snake(text):
    if not any (i.isupper() for i in text):
        print(text)
    else:
        print(underscore(text))

def underscore(text):

    up_index = []

    for i in text:
        if i.isupper() == True:
            up_index.append(text.index(i))

    for k in sorted(up_index, reverse=True):
        text = text[:k] + "_" + text[k:]

    return text.lower()

main()
