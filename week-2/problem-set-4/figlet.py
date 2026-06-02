import sys
import random
import pyfiglet

if len(sys.argv) == 1:
    text = input("Input: ").strip()
    print(pyfiglet.figlet_format(text, font=random.choice(pyfiglet.FigletFont.getFonts())))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in pyfiglet.FigletFont.getFonts():
        text = input("Input: ").strip()
        print(pyfiglet.figlet_format(text, font=sys.argv[2]))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

