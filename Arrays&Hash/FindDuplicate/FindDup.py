def hasDuplicate(nums):
    
    checker = {}
    for num in nums:
        if num in checker:
            return True
        checker[num] = 1
    
    return False


hasDuplicate([1, 2, 3, 3])