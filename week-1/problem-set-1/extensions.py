ex = input("File name: ")
ex = ex.strip(" ").lower()

if ex.endswith(".gif") == True:
    print ("image/gif")
elif ex.endswith(".jpg") == True or ex.endswith(".jpeg") == True:
    print ("image/jpeg")
elif ex.endswith(".png") == True:
    print ("image/png")
elif ex.endswith(".pdf") == True:
    print ("application/pdf")
elif ex.endswith(".txt") == True:
    print ("text/plain")
elif ex.endswith(".zip") == True:
    print ("application/zip")
else:
    print ("application/octet-stream")
