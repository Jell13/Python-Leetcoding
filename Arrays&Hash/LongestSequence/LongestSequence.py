def longestConsecutive(nums):

    sNums = set(nums)
    counter = 0
    for num in sNums:
        count = 0
        if (num - 1) in sNums:
            continue
        count += 1
        while (num + count) in sNums:
            count += 1

        counter = max(counter, count)

    return counter

print(longestConsecutive([2,20,4,10,3,4,5]))

