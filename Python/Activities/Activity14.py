def fib(num):
    if(num<=1):
        return num
    else:
        return (fib(num-1)+fib(num-2))
    
num = int(input("Enter the number: "))

if(num<0):
    print("Enter a positive number!!")
else:
    print("Fibonacci Sequence: ")
    for i in range(num):
        print(fib(i),end=" ")

