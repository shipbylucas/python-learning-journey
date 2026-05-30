def main():
    percent = fuel_gauge()
    print (percent)

def fuel_gauge():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = numer(x)
            y = deno(y)
            if 1 >= x/y >= 0.99:
                return "F"
            elif 0.01 < x/y < 0.99:
                return (str(round(x/y * 100)) + "%")
            elif x/y <= 0.01:
                return "E"
        except:
            continue

def numer(m):
    try:
        m = int(m)
        if m >= 0:
            return m
        else:
            pass
    except ValueError:
        pass

def deno(n):
    try:
        n = int(n)
        if n > 0:
            return n
        else:
            pass
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

main()
