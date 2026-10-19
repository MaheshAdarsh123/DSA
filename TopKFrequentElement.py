def topKFrequentElement(nums,k):
    count = {} # this is how you define a dictionary in PY

    for num in nums:
        count[num] = count.get(num,0)+1

    result = sorted(count, key=count.get, reverse=True)
    return result[:k]


# nums = list(map(int, input('Enter number --> ').split()))
# k = int(input('Enter target --> '))
print(topKFrequentElement([5, 5, 5, 2, 2, 3, 3, 3, 3], 2))