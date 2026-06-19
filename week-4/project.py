import requests
import csv
from tabulate import tabulate
import os

# Get id list
idUrl = "https://api.coingecko.com/api/v3/coins/list"
headers = {"x-cg-demo-api-key": "CG-WUYhWseXr3Hif4WyegsL36mT"}

response = requests.get(idUrl, headers=headers)
idData = response.json()

idList = [project["id"] for project in idData]

tracker = "Crypto P&L Tracker"
infor = ["ID", "Holdings", "Principal", "Today's Value"]

if not os.path.exists(f"{tracker}.csv"):
    with open(f"{tracker}.csv", "w") as nFile:
        writer = csv.DictWriter(nFile, fieldnames=infor)
        writer.writeheader()

def main():
    print("Welcome back, Long")

    bID = bAmount = bQuantity = None
    sID = sAmount = sQuantity = None

    totalPrincipal = 0
    totalValue = 0

    with open(f"{tracker}.csv") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    existing_ids = [row["ID"] for row in rows]

    status = checker()
    if status == "Buy":
        bID, bAmount = buyAmount()
        bQuantity = bAmount / float(getPrice(bID))
    elif status == "Sell":
        sID, sAmount = sellAmount(existing_ids, rows)
        sQuantity = sAmount / float(getPrice(sID))
    elif status == "Both":
        bID, bAmount = buyAmount()
        bQuantity = bAmount / float(getPrice(bID))
        sID, sAmount = sellAmount(existing_ids, rows)
        sQuantity = sAmount / float(getPrice(sID))

    if rows:     
        if status == "Chilling": 
            print(f"Gotcha! The market is tough, right?")
        else:
            for row in rows:
                if row["ID"] == bID or row["ID"] == sID:
                    if status == "Buy":
                        row["Holdings"] = float(row["Holdings"]) + bQuantity
                        row["Principal"] = float(row["Principal"]) + bAmount
                    elif status == "Sell":
                        row["Holdings"] = float(row["Holdings"]) - sQuantity
                        row["Principal"] = float(row["Principal"]) - sAmount
                    elif status == "Both":
                        if row["ID"] == bID:
                            row["Holdings"] = float(row["Holdings"]) + bQuantity
                            row["Principal"] = float(row["Principal"]) + bAmount
                        if row["ID"] == sID:
                            row["Holdings"] = float(row["Holdings"]) - sQuantity
                            row["Principal"] = float(row["Principal"]) - sAmount
                    row["Today's Value"] = float(row["Holdings"]) * getPrice(row["ID"])
            with open(f"{tracker}.csv", "w") as wFile:
                writer = csv.DictWriter(wFile, fieldnames=infor)
                writer.writeheader()
                writer.writerows(rows)
            if bID and bID not in existing_ids:
                with open(f"{tracker}.csv", "a") as mFile:
                    m = csv.DictWriter(mFile, fieldnames=infor)
                    m.writerow({"ID":bID, "Holdings":bQuantity, "Principal":bAmount, "Today's Value":bQuantity * getPrice(bID)})
    else:
        with open(f"{tracker}.csv", "a") as kFile:
            first = csv.DictWriter(kFile, fieldnames=infor)
            if bID != None:
                first.writerow({"ID":bID, "Holdings":bQuantity, "Principal":bAmount, "Today's Value": bQuantity * getPrice(bID)})
            if sID != None:
                first.writerow({"ID":sID, "Holdings":sQuantity, "Principal":sAmount, "Today's Value": sQuantity * getPrice(sID)})
    
    with open(f"{tracker}.csv") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for h in rows:
        totalPrincipal += float(h["Principal"])
        totalValue += float(h["Today's Value"])

    if totalPrincipal == 0:
        print("Oops! You don't have any positions to show yet. Try buying some assets to get started.")
    else:
        ROI = (float(totalValue) - float(totalPrincipal)) / float(totalPrincipal) * 100 - 1
        print(f"Here's your current {tracker}:")
        print(tabulate(rows, headers="keys", tablefmt="grid"))
        print(f"-> ROI = {ROI:.2f}%")

def checker():
    while True:
        status = input("Do you buy, sell, or both today? \nIf you do nothing, type 'Chilling'\n").strip().capitalize()
        if status == "Buy":
            return "Buy"
        elif status == "Sell":
            return "Sell"
        elif status == "Both":
            return "Both"
        elif status == "Chilling":
            return "Chilling"
        else:
            print("Invalid command")
            continue

def buyAmount():
    while True:
        try:
            id = input("What did you buy today? ").strip().lower()
            if id in idList:
                dollarAmount = float(input("How much did you buy in $? "))
                return (id, dollarAmount)
            else:
                print("Invalid id")
                continue
        except ValueError:
            print("Invalid amount")
            continue

def sellAmount(existing_ids, rows):
    while True:
        try:
            id = input("What did you sell today? ").strip().lower()
            if id not in existing_ids:
                print("You don't have this position to sell!")
                continue
            else:
                if id in idList:
                    dollarAmount = float(input("How much did you sell in $? "))
                    for row in rows: 
                        if row["ID"] == id:
                            if dollarAmount > float(row["Today's Value"]):
                                print("Insufficient balance.")
                                continue
                        else:
                            return (id, dollarAmount)
                else:
                    print("Invalid id")
                    continue
        except ValueError:
            print("Invalid amount")
            continue
        
def getPrice(id):
    priceUrl = "https://api.coingecko.com/api/v3/simple/price"
    headers = {"x-cg-demo-api-key": "CG-WUYhWseXr3Hif4WyegsL36mT"}
    params = {
        "ids": id,
        "vs_currencies": "usd"
    }
    response = requests.get(priceUrl, headers=headers, params=params)
    priceData = response.json()
    return priceData[id]["usd"]

if __name__ == "__main__":
    main() 