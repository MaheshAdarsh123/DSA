number = int(input("Enter a number: "))
count = 0

while number > 0:

    count += 1
    number = number//10

print(count)

# from math import log10, floor
# def count_digits(number):
#     if number == 0:
#         return 1
#     return int(log10(abs(number))) + 1