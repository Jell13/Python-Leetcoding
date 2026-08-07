def carFleet(target, position, speed):
    pairs = [(position[i], speed[i]) for i in range(len(position))]
    pairs.sort(reverse=True)

    checker = []
    res = 0

    for (pos, spd) in pairs:
        time = (target - pos) / spd
        if checker and time > checker[-1]:
            checker.append(time)

    return len(checker)