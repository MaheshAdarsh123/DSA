num = int(input("Enter a number: "))
factorial = 1

if num <=1:
    print("The factorial of", num, "is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)