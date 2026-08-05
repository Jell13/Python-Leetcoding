def trap(height):
    l, r = 0, len(height) - 1

    leftMax = height[l]
    rightMax = height[r]
    totalWater = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            totalWater += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            totalWater += rightMax - height[r]

    return totalWater

