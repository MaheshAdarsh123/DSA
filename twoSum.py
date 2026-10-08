def twoSum(numbers, target):

    seen = {}
    for i in range(len(numbers)):

        
        complement  = target - numbers[i]
        if complement in seen:
            return [seen[complement],i]

        seen[numbers[i]] = i

numbers = list(map(int, input('Enter number --> ').split()))
target = int(input('Enter target --> '))

print(twoSum(numbers, target))
        
        
