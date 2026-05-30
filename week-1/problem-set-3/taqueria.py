menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    bill = order()
    print(bill)

def order():
    total = 0
    while True:
        try:
            dish = input("Item: ").strip().title()
            total = total + menu[dish]
            print ("Total: " + "$" + f"{total:.2f}")
            continue
        except EOFError:
            break
        except:
            continue

main()
