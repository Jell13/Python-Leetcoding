def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    A, B = nums1, nums2
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2

    low, high = 0, m - 1
    while True:
        i = (low + high) // 2
        j = half - 2 - i

        A_left = A[i] if i >= 0 else float('-inf')
        A_right = A[i + 1] if i + 1 < m else float('inf')
        B_left = B[j] if j >= 0 else float('-inf')
        B_right = B[j + 1] if j + 1 < n else float('inf')

        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 0:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            else:
                return max(A_left, B_left)
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1
 