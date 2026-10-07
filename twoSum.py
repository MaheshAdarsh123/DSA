def twoSum(numbers, target):

    asx = 0
    seen = set()
    for num in numbers:
        asx = target - num
        if asx in seen:
            return True
        
