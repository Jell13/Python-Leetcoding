from collections import defaultdict

def groupAnagrams(strs):
    counter = defaultdict(list)

    for st in strs:
        key = [0] * 26
        for char in st:
            key[ord(char) - ord('a')] += 1
        counter[tuple(key)].append(st)

    return list(counter.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))