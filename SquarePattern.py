num = int(input("Enter a number: "))

if(num > 0):
    i=1
    for i in range(num):
        for j in range(num):
            print(i, end=" ")
        print()