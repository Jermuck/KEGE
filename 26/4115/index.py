with open("26_4115.txt") as f:
    N = int(f.readline());
    points = [];
    for _ in range(N):
        x, y = map(int, f.readline().split());
        points += [(x, y)];
points.sort();
mx = 0;
for x in range(N):
    k = 1;
    s = points[x]
    for y in range(x + 1, N):
        if s[0] == points[y][0] and s[1] + 1 == points[y][1]:
            k += 1;
            s = points[y]
    if k > mx:
        num = s[0]
    mx = max(mx, k);
print(mx, num) # 7 5562 