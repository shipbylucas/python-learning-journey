def main ():
    answer = input("What's the input? ")
    print(convert(answer))

def convert(text):
    return text.replace(":)","🙂").replace(":(","🙁")

main()
