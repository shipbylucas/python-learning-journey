text = input("Greet: ")
text = text.strip(" ").lower()
if text.startswith("h") == True:
    print ("$0") if text.startswith("hello") == True else print ("$20")
else:
    print ("$100")
