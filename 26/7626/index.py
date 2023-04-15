with open("26_7626.txt") as f:
    k = int(f.readline());
    n = int(f.readline());
    points = [];
    for _ in range(n):
        x, y = map(int, f.readline().split());
        points += [(x, y)];
points.sort();
kamera = [(0, 0)] * k;
count = 0;
for x in range(n):
    for z in range(k):
        if kamera[z][1] < points[x][0]:
            kamera[z] = (0, 0); 
    free = [idx for idx in range(k) if kamera[idx] == (0, 0)];
    if len(free) != 0:
        kamera[min(free)] = points[x];
        last = min(free) + 1;
        count += 1;
print(count, last);