import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = re.search(r"^(?P<start>([\d]\d?)(:\d\d)? (AM|PM)) to (?P<end>(\d\d?)(:\d\d)? (AM|PM))$", s)
    if pattern:
        if not hour_format(pattern.group(2)) or not hour_format(pattern.group(6)) or not min_format(pattern.group(3)) or not min_format(pattern.group(7)):
            raise ValueError
        else:
            start = to24(pattern.group("start"))
            end = to24(pattern.group("end"))
            return (f"{start} to {end}")
    else:
        raise ValueError

def to24(time):
    match = re.search(r"(^[\d]\d?)(:\d\d)? (AM|PM)$", time)
    minute = match.group(2)
    if minute == None:
        minute = ":00"
    hour = match.group(1)
    part = match.group(3)
    if part == "AM":
        if len(hour) == 1:
            return (f"0{hour}{minute}")
        elif len(hour) == 2:
            if hour == "12":
                return (f"00{minute}")
            else:
                return (f"{hour}{minute}")
    elif part == "PM":
        if hour == "12":
            return (f"12{minute}")
        else:
            return (f"{int(hour) + 12}{minute}")

def hour_format(h):
    if len(h) == 1 and int(h[0]) in range (1,10):
        return True
    elif len(h) == 2 and int(h) in [10, 11, 12]:
        return True
    else:
        return False

def min_format(m):
    if m == None:
        return True
    else:
        m = m.lstrip(":")
        if int(m) in range (0,60):
            return True
        else:
            return False

if __name__ == "__main__":
    main()
