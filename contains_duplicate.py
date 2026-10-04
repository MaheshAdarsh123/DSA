def contains_duplicate(numbers):
    asx = set()

    for number in numbers:
        if number in asx:
            return 'Duplicate present: ' + str(number)
        asx.add(number)

    return 'No Duplicate'


numbers = list(map(int, input('Enter number: ').split()))
print(contains_duplicate(numbers))

