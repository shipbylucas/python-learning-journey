def main():
    tweet = input("Input: ")
    tweet_content(tweet)

def tweet_content(text):
    for i in text:
        if i in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            text = text.replace(i, "")
    print("Output:", text)

main()
