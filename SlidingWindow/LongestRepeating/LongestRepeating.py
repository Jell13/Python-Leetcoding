def characterReplacement(s, k):
    l = 0
    counter = {}
    maxFreq = 0
    result = 0

    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1
        maxFreq = max(maxFreq, counter[s[r]])
        windowLength = r - l + 1

        if (windowLength - maxFreq) > k:
            counter[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)
    return result

print(characterReplacement("AAABABB", 1))
