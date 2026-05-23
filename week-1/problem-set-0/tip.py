def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    payment = d.lstrip('$')
    ans = float(payment)
    return round(ans, 1)

def percent_to_float(p):
    tip = p.rstrip('%')
    return int(tip) / 100

main()
