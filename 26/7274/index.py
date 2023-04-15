with open('26_7274.txt') as f:
    N = int(f.readline());
    points = [];
    for _ in range(N):
        row, place = map(int, f.readline().split());
        points += [(row, place)];
points.sort();
mx = 0;
mn_place = 10 ** 20
for x in range(N - 1):
    a, b = points[x], points[x+1];
    if a[0] == b[0] and b[1] - a[1] == 14:
        if a[0] == 59966:
            print(a, b)
        mx = max(a[0], mx);
print(mx) # 59966 50448 + 1