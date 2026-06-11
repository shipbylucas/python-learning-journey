import re

def main():
    print(count(input("Text: ")))

def count(s):
    count = 0
    word = s.split(" ")
    for i in word:
        pattern = re.search(r"^um\W*$", i, re.IGNORECASE)
        if pattern:
            count += 1
    return count

if __name__ == "__main__":
    main()
