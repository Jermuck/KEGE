with open("26_7456.txt") as f:
    n = int(f.readline());
    points = [];
    for _ in range(n):
        x, y = map(int, f.readline().split());
        points += [(x, y)];
points.sort();
k = 0;
mx = 0;
for x in range(n - 2):
    a, b, c = points[x], points[x+1], points[x+2];
    if a[0] == b[0] and b[0] == c[0] and b[1] - a[1] == 6 and c[1] - b[1] == 6:
        k += 1;
        mx = max(mx, a[0]);
print(mx, k) # 4896 17