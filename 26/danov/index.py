with open("test.txt") as f:
    k = int(f.readline());
    n = int(f.readline());
    points = [];
    for _ in range(n):
        x, y = map(int, f.readline().split());
        points.append((x, y));
points.sort();
kamera = [(0, 0)] * k
tec = 0
for x in range(n):
    for y in range(k):
        if points[x][0] > kamera[y][1]:
            kamera[y] = (0, 0);
    free = [z for z in range(k) if kamera[z] == (0, 0)];
    if len(free) > 0:
        max_idx = max(free);
        kamera[max_idx] = points[x];
        print(kamera)
        tec = max_idx + 1;
print(tec)