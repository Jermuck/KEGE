with open("26(1).txt") as f:
    N = int(f.readline());
    points = [];
    for _ in range(N):
        row, place = map(int, f.readline().split());
        points += [(row, place)];
points.sort();
mx = k = 0
for x in range(1, N - 1):
    a, b, c = points[x-1], points[x], points[x+1];
    if a[0] == b[0] and a[0] == c[0] and b[0] == c[0] and \
        (b[1] - a[1] == 6 and c[1] - b[1] == 6):
        k += 1
        if b[0] > mx:
            mx = b[0];
print(mx, k)