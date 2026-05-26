def main():
    t = input("What time is it? ").strip()

    if t.endswith("a.m."):
        t = t.rstrip("a.m.").strip()
        if 7 <= convert(t) <= 8:
            print ("breakfast time")

    elif t.endswith("p.m."):
        t = t.rstrip("p.m.").strip()
        if 12 <= convert(t) <= 13:
            print ("lunch time")
        elif 18 <= convert(t) + 12 <= 19:
            print ("dinner time")

    else:
        if 7 <= convert(t) <= 8:
            print ("breakfast time")
        if 12 <= convert(t) <= 13:
            print ("lunch time")
        if 18 <= convert(t) <= 19:
            print ("dinner time")

def convert(time):
    hr,min = time.split(":")
    return int(hr) + int(min) / 60

if __name__ == "__main__":
    main()
