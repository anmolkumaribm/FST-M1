newDict=  {"mango":25,"apple":14,"kiwi":37,"orange":55}

x = input("Enter fruit name: ").lower()
if(x in newDict):
    print(x,"is present")
else:
    print(x,"is absent")