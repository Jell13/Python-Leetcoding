def lengthOfLongestSubstring(s):
    track = set()
    maxLen = 0
    l, r = 0, 0

    while r < len(s):
        if s[r] in track:
            track.remove(s[l])
            l += 1
        else:
            track.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1

    return maxLen

print(lengthOfLongestSubstring("pwwkew"))

        