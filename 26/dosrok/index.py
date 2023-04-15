with open("26_7602.txt") as f:
    K = int(f.readline());
    N = int(f.readline());
    points = []
    for _ in range(N):
        st, end = map(int, f.readline().split());
        points += [(st, end)];
points.sort()
k = 0;
last = 0;
kamera = [(0, 0)] * K;

for x in range(N):
    for j in range(K):
        if kamera[j][1] < points[x][0]:
            kamera[j] = (0, 0);
    free = [idx for idx in range(len(kamera)) if kamera[idx] == (0, 0)];
    if len(free) > 0:
        k += 1;
        last = min(free);
        kamera[last] = points[x];
print(k, last + 1)
