with open("27_B_7275.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = [0] * 10 ** 7
    for _ in range(N):
        km, k = map(int, f.readline().split());
        c = k // 30 if k % 30 == 0 else k // 30 + 1
        points[km] = c;
mx = s = sum(points[0:2 * LIM + 1]);
for x in range(1, len(points) - 2 * LIM):
    s = s - points[x-1] + points[x + 2 * LIM];
    if points[x + LIM] != 0:
        mx = max(mx, s);
print(mx) # 27140