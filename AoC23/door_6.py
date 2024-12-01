time = [46689866]
distance = [358105418071080]

l = []
for i in range(0, len(time)):
    t = time[i]
    best = distance[i]
    ways_to_beat = 0
    for sec in range(1, t):
        time_left = t - sec
        speed = sec
        x = speed * time_left

        if x <= best:
            continue
        ways_to_beat += 1

    l.append(ways_to_beat)

print(l)

result = 1
for x in l:
    result = result * x
print(result)