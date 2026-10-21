def topKFrequentElement(nums,k):
    count = {} # this is how you define a dictionary in PY

    for num in nums:
        count[num] = count.get(num,0)+1

    result = sorted(count, key=count.get(num,0), reverse=True) # sorted(iterable, key=None, reverse=False)
    return result[:k]

# iterable: The sequence to be sorted (list, tuple, set, string, etc.)
# key (Optional): A function to customize the sort order. Default is None.
# reverse (Optional): If True, sorts in descending order. Default is False.


nums = list(map(int, input('Enter number --> ').split()))
k = int(input('Enter target --> '))
print(topKFrequentElement(nums, k))