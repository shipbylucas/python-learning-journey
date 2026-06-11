import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = re.search(r'^<iframe(.+|\s)?src="(.+)"(.+|\s)?></iframe>$', s)
    if pattern:
        link = pattern.group(2)
        match = re.search(r"https?://(www\.)?youtube\.com/embed/(\w+)", link)
        if match:
            return (f"https://youtu.be/{match.group(2)}")
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    main()
