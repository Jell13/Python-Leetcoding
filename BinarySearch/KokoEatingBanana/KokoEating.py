def minEatingSpeed(piles, h):

    def hoursNeeded(k):
        total = 0
        for pile in piles:
            total += (pile + (k - 1)) // k
        return total
    
    low, high = 1, max(piles)
    result = high
    while low <= high:
        m = low + (high - low) // 2
        hours = hoursNeeded(m)
        if hours > h:
            low = m + 1
        elif hours <= h:
            result = m
            high = m - 1

    return result
