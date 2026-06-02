import random
import sys

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        attempt = 0
        while attempt < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == x + y:
                    score += 1
                    break
                else:
                    attempt += 1
                    print("EEE")
            except ValueError:
                attempt += 1
                print("EEE")
            except EOFError:
                print(f"Score: {score}")
                sys.exit(0)
        else:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except EOFError:
            sys.exit(0)
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
