def largestRectangleArea(heights):

    stack = []
    maxArea = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            width = i - idx
            maxArea = max(maxArea, width * height)
            start = idx

        stack.append((start, h))

    for idx, height in stack:
        width = len(heights) - idx
        maxArea = max(maxArea, height * width)

    return maxArea

print(largestRectangleArea([7,1,7,2,2,4]))