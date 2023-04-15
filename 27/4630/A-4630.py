with open("27A_4630.txt") as f:
    N, WAY, LIM = map(int, f.readline().split());
    points = [];
    for _ in range(N):
        km, k = map(int, f.readline().split());
        c = k // 9 if k % 9 == 0 else k // 9 + 1;
        points += [(km, c)];
mx = 0;
for x in range(N):
    s = 0;
    for y in range(N):
        if min(abs(points[x][0] - points[y][0]), WAY - abs(points[x][0] - points[y][0])) <= LIM:
            s += points[y][1];
    mx = max(mx, s);
print(mx) # 409