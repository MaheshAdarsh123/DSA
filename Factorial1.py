num = int(input("Enter a number: "))
factorial = 1
if num > 0:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}") 
else:
    print("Factorial is not defined for negative numbers or zero.")