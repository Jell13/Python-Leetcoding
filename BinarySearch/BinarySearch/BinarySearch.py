def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(search([-1,0,2,4,6,8], 4))
        