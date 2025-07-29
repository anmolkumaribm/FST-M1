newTuple = input("Enter the number tuple: ").split(",")

for x in newTuple:
    if(int(x)%5==0):
        print(x)