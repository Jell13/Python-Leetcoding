def encode(strs):
    res = []
    for s in strs:
        res.append(str(len(s)))
        res.append('#')
        res.append(s)

    return "".join(res)

def decode(str):
    res = []

    i = 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = str[i:j]
        i = j + 1
        j = i + length

        res.append(str[i:j])
        i = j

    return res

print(encode(["Hello","World"]))