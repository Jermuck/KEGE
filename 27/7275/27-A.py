with open("27_A_7275.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = [];
    for _ in range(N):
        km, k = map(int, f.readline().split());
        c = k // 30 if k % 30 == 0 else k // 30 + 1
        points += [(km, c)];
mx = 0;
for x in range(N):
    s = 0;
    for y in range(N):
        r = abs(points[x][0] - points[y][0]);
        if r <= LIM:
            s += points[y][1];
    mx = max(mx, s);
print(mx) # 264