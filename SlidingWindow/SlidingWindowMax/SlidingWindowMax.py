from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    result = []

    l = 0
    for r in range(len(nums)):
        while dq and nums[dq[-1]] < nums[r]:
            dq.pop()
        dq.append(r)

        l = r - k + 1
        if dq and dq[0] < l:
            dq.popleft()

        if r + 1 >= k:
            result.append(nums[dq[0]])

    return result
        