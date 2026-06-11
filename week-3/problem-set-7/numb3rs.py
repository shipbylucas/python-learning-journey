import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = re.search(r"^(\d(?:\d)?(?:\d)?)\.(\d(?:\d)?(?:\d)?)\.(\d(?:\d)?(?:\d)?)\.(\d(?:\d)?(?:\d)?)$", ip)
    if pattern:
        for i in range (1,5):
            if not (0 <= int(pattern.group(i)) <= 255):
                return False
        else:
            for i in range(1,5):
                if zero_yes(pattern.group(i)):
                    return False
            else:
                return True
    else:
        return False

def zero_yes(num):
    if num.startswith("0"):
        if num == "0":
            return False
        else:
            return True

if __name__ == "__main__":
    main()
