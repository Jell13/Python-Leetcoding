def minWindow(s, t):
    if not t:
        return ""

    need = {} 
    for c in t:
        need[c] = need.get(c, 0) + 1

    have, l = 0, 0
    need_count = len(need)
    result = None
    window = {}
    resultLen = float('inf')

    for r in range(len(s)):
        char = s[r]
        window = window.get(char, 0) + 1
        if char in need and window[char] == need[char]:
            have += 1
        while have == need_count:
            if r - l + 1 < resultLen:
                result = (l, r)
                resultLen = r - l + 1

            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    if result == None:
        return ""

    l, r = result
    return s[l : r]
        