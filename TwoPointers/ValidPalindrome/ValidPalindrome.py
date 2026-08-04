def validPalindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        if alphaNum(s[l]) and alphaNum(s[r]):
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        elif alphaNum(s[l]) == False:
            l += 1
        elif alphaNum(s[r]) == False:
            r -= 1

    return True

def alphaNum(c):
    return ((ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9')))