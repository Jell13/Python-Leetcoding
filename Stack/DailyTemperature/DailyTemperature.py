def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    counter = []

    for i, temp in enumerate(temperatures):
        while counter and temp > counter[-1][1]:
            idx, tem = counter.pop()
            res[idx] = i - idx

        counter.append(tuple((i, temp)))

    return res