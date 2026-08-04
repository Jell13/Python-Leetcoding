def twoSum(nums, target):

    checker = {}
    for i in range(len(nums)):
        if (target - nums[i]) in checker:
            return [checker[target-nums[i]], i]
        else:
            checker[nums[i]] = i

print(twoSum([3,4,5,6], 7))