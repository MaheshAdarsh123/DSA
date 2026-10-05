def contains_duplicate(nums,k):
    asx = set()
    #[1,2,3,1] K = 2
    for i in range(len(nums)):
        if nums[i] in asx:
            return True
        
        asx.add(nums[i])


        if i >= k:
            asx.remove(nums[i-k])

    return False

nums = list(map(int, input('Enter Number:  ').split()))
k = int(input('Enter range: '))

print(contains_duplicate(nums,k))
            
