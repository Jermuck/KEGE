with open("27_A_7097.txt") as f:
    N = int(f.readline());
    points = [];
    for _ in range(N):
        km, k = map(int, f.readline().split());
        c = k // 44 if k % 44 == 0 else k // 44 + 1;
        points.append((km, c));
mn = 10 ** 50;

for x in range(N):
    s = 0
    for y in range(N):
        r = abs(points[x][0] - points[y][0]) * points[y][1];
        s += r;
    mn = min(mn, s);
print(mn)