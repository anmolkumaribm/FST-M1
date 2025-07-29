numlist = input("Enter the numbers seperated by comma: ").split(",")
sum=0

for x in numlist:
    sum+=int(x)

print(numlist)
print("sum of list is: ", sum)