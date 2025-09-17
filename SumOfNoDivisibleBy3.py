num = int(input("Enter number "))
if(num>3):
    K = num//3
    sum = 3 * (K * (K + 1)//2)
    print("Sum of numbers divisible by 3 is", sum)
else:
    print("Sum of numbers divisible by 3 is 0")

if(num>5):
    L = num//5
    sum5 = 5 * (L * (L + 1)//2)
    print("Sum of numbers divisible by 5 is", sum5)
else:
    print("Sum of numbers divisible by 5 is 0")