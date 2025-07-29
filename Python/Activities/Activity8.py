numlist = input("Enter the numbers seperated by comma: ").split(",")

print(numlist)
if(numlist[0]==numlist[-1]):
    print(True)
else:
    print(False)