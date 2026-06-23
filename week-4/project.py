import requests
import csv
from tabulate import tabulate
import os
from dotenv import load_dotenv

load_dotenv()

# Get id list
idUrl = "https://api.coingecko.com/api/v3/coins/list"
headers = {"x-cg-demo-api-key": "COINGECKO_API_KEY"}

response = requests.get(idUrl, headers=headers)
idData = response.json()

idList = [project["id"] for project in idData]

tracker = "Crypto P&L Tracker"
infor = ["ID", "Holdings", "Avg Price", "Balance", "Today's Price"]

if not os.path.exists(f"{tracker}.csv"):
    with open(f"{tracker}.csv", "w") as nFile:
        writer = csv.DictWriter(nFile, fieldnames=infor)
        writer.writeheader()

def main():
    print("Welcome back, Long")

    bID = bEntry = bBought = None
    sID = sLeft = None

    totalInvest = 0
    todayValue = 0

    with open(f"{tracker}.csv") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    existing_ids = [row["ID"] for row in rows]

    status = checker()
    if status == "Buy":
        bID, bEntry, bBought = buyAmount(existing_ids, rows)
    elif status == "Sell":
        sID, sLeft = sellAmount(existing_ids, rows)
    elif status == "Both":
        bID, bEntry, bBought = buyAmount(existing_ids, rows)
        sID, sLeft = sellAmount(existing_ids, rows)

    if rows:     
        if status == "Chilling": 
            print(f"Got it. The market can be tough sometimes, right?")
        else:
            for row in rows:
                if row["ID"] == bID or row["ID"] == sID:
                    if status == "Buy":
                        row["Holdings"] = float(row["Holdings"]) + bBought
                    elif status == "Sell":
                        row["Holdings"] = sLeft
                    elif status == "Both":
                        if row["ID"] == bID:
                            row["Holdings"] = float(row["Holdings"]) + bBought
                        if row["ID"] == sID:
                            row["Holdings"] = sLeft
                    row["Today's Price"] = getPrice(row["ID"])
                    row["Balance"] = float(row["Holdings"]) * float(row["Today's Price"])
                    if row["ID"] == bID and bEntry is not None:
                        row["Avg Price"] = bEntry
            with open(f"{tracker}.csv", "w") as wFile:
                writer = csv.DictWriter(wFile, fieldnames=infor)
                writer.writeheader()
                writer.writerows(rows)
            if bID and bID not in existing_ids:
                new_row = {"ID":bID, "Holdings":bBought, "Avg Price":bEntry, "Balance":bBought * getPrice(bID), "Today's Price":getPrice(bID)}
                rows.append(new_row)
            for row in rows:
                row["Today's Price"] = getPrice(row["ID"])
                row["Balance"] = float(row["Holdings"]) * float(row["Today's Price"])
            with open(f"{tracker}.csv", "w") as wFile:
                writer = csv.DictWriter(wFile, fieldnames=infor)
                writer.writeheader()
                writer.writerows(rows)
    else:
        with open(f"{tracker}.csv", "a") as kFile:
            first = csv.DictWriter(kFile, fieldnames=infor)
            if bID != None:
                first.writerow({"ID":bID, "Holdings":bBought, "Avg Price":bEntry, "Balance":bBought * getPrice(bID), "Today's Price":getPrice(bID)})

    with open(f"{tracker}.csv") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for h in rows:
        invest = float(h["Avg Price"]) * float(h["Holdings"])
        totalInvest += float(invest)
        value = float(h["Today's Price"]) * float(h["Holdings"])
        todayValue += float(value)

    if totalInvest == 0:
        print("Oops! You don't have any positions to show yet. Try buying some assets to get started.")
    else:
        ROI = (float(todayValue) - float(totalInvest)) / float(totalInvest) * 100
        print(f"Here's your current {tracker}:")
        print(tabulate(rows, headers="keys", tablefmt="grid"))
        print(f"-> ROI = {ROI:.2f}%")

def checker():
    while True:
        status = input("Did you buy, sell, or both today? \nIf you didn't make any trades, type 'Chilling'\n").strip().capitalize()
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

def buyAmount(existing_ids, rows):
    while True:
        try:
            id = input("What did you buy today? ").strip().lower()
            if id in idList:
                dollarAmount = float(input("How much did you buy ($)? "))
                if id not in existing_ids:
                    entry = getPrice(id)
                    holding = dollarAmount / entry
                    return (id, entry, holding)
                else:
                    for row in rows:
                        if row["ID"] == id:
                            bPrice = getPrice(id)
                            bHolding = dollarAmount / bPrice
                            bEntry = (float(row["Avg Price"]) * float(row["Holdings"]) + dollarAmount)/(float(row["Holdings"]) + bHolding)
                    return (id, bEntry, bHolding)
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
                    dollarAmount = float(input("How much did you sell ($)? "))
                    for row in rows: 
                        if row["ID"] == id:
                            balance = float(row["Today's Price"]) * float(row["Holdings"])
                            if dollarAmount > balance:
                                print(f"Insufficient balance. Your {id} balance is ${balance:.2f}.")
                                break
                            else:
                                sPrice = getPrice(id)
                                sLeft = float(row["Holdings"]) - dollarAmount / sPrice
                                return (id, sLeft)
                else:
                    print("Invalid id")
                    continue
        except ValueError:
            print("Invalid amount")
            continue
        
def getPrice(id):
    priceUrl = "https://api.coingecko.com/api/v3/simple/price"
    headers = {"x-cg-demo-api-key": "COINGECKO_API_KEY"}
    params = {
        "ids": id,
        "vs_currencies": "usd"
    }
    response = requests.get(priceUrl, headers=headers, params=params)
    priceData = response.json()
    return priceData[id]["usd"]

if __name__ == "__main__":
    main() 