import sys
from PIL import Image, ImageOps

if len(sys.argv) in [1, 2]:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    if sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) == False:
        sys.exit("Invalid input")
    elif sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")) == False:
        sys.exit("Invalid output")
    elif sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")
    elif sys.argv[1][-4:] == sys.argv[2][-4:]:
        try:
            with Image.open(sys.argv[1]) as input, Image.open("shirt.png") as shirt:
                resize = ImageOps.fit(
                    input,
                    shirt.size,
                    method=Image.Resampling.BICUBIC,
                    bleed=0.0,
                    centering=(0.5,0.5),
                )
                resize.paste(shirt, (0,0), shirt)
                resize.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")