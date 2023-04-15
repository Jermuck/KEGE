with open("26_7690.txt") as f:
    N, K, LIM = map(int, f.readline().split());
    points = [];
    for _ in range(N):
        a, b = map(int, f.readline().split());
        points += [(a, b)];
mx_start = min(x for x in points if x[1] == K);
points.sort()
mx_start_index = points.index(mx_start);
points = points[mx_start_index:];
arr = [mx_start]
for x in range(1, len(points) - LIM):
    tec_mx = (0, 0)
    srez = points[x: x + LIM]
    for z in srez:
        if z[1] >= K and z[0] > arr[-1][0] and abs(arr[-1][0] - z[0]) <= LIM:
            if z[0] > tec_mx[0]:
                tec_mx = z;
    if tec_mx != (0, 0):
        arr.append(tec_mx)
print(len(arr), arr[-1][0]) # 234 468