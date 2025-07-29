numlist1 = input("Enter the numbers seperated by comma: ").split(",")
numlist2 = input("Enter the numbers seperated by comma: ").split(",")

numlist3 = []

for i in numlist1:
    if(int(i) %2 !=0):
        numlist3.append(i)

for j in numlist2:
    if(int(j)%2 == 0):
        numlist3.append(j)

print("new List: ",numlist3)