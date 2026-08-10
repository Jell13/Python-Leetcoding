def searchMatrix(matrix, target):
    l, r = 0, len(matrix) - 1
    idx = -1
    while l <= r:
        m = l + (r - l) // 2
        if target < matrix[m][0]:
            r = m - 1
        elif target > matrix[m][-1]:
            l = m + 1
        else:
            idx = m
            break

    if idx == -1:
        return False
    
    curr = matrix[idx]
    left, right = 0, len(curr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if curr[mid] == target:
            return True
        elif curr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

    