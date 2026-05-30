def main():

    total = 50

    while True:
        insert_amount = int(input("Insert Coin: "))
        if insert_amount in [25, 10, 5]:
            total = total - insert_amount
            if total > 0:
                print("Amount Due:", total)
                continue
            elif total <= 0:
                print("Change Owed:", 0 - total)
                break
        else:
            if total > 0:
                print("Amount Due:", total)
                continue
            elif total <= 0:
                print("Change Owed:", 0 - total)
                break

main()

