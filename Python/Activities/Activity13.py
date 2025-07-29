def sum(nums):
    temp=0
    print("Given list: ",nums)
    for i in nums:
        temp+=int(i)
    print("Sum of all the elements of the list: ",temp)
nums = input("Enter number list with comma seperated: ").split(",")

sum(nums)
