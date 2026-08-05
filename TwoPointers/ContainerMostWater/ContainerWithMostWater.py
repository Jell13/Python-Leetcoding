def maxArea(heights):
    l, r = 0, len(heights) - 1
    mArea = 0

    while l < r:
        minH = min(heights[l], heights[r])
        length = r - l
        area = minH * length

        mArea = max(area, mArea)

        if heights[l] < heights[r]:
            l += 1
        elif heights[r] < heights[l]:
            r -= 1

        else:
            l += 1
            r -= 1

    return mArea
         