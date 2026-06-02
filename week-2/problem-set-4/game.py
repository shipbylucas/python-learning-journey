import random

def main():
    ans = game()
    print(ans)

def game():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                target = random.randint(1,level)
                return guess(target)
            else: continue
        except: continue

def guess(num):
    while True:
        try:
            guess = int(input("Guess: "))
            if 0 < guess < num:
                print ("Too small!")
                continue
            elif num < guess:
                print ("Too large!")
                continue
            elif num == guess:
                return ("Just right!")
            else: continue
        except: continue

main()

