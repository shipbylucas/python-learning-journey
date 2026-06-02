import emoji

text = input("Input: ").strip()

if emoji.emojize(text) != text:
    print("Output: ", emoji.emojize(text))
else:
    print("Output: ", emoji.emojize(text, language = "alias"))
