with open("27A_6638.txt") as f:
    N = int(f.readline());
    points = [];
    for _ in range(N):
        Id, k = map(int, f.readline().split());
        c = k // 100 if k % 100 == 0 else k // 100 + 1;
        points += [(Id, c)];
mn = 10 ** 10;
res_Id = 90;
for x in range(N):
    s = 0;
    for y in range(N):
        r = abs(points[x][0] - points[y][0]) * points[y][1];
        s += r;
    if s < mn:
        mn = s;
        res_Id = points[x][0] 
print(res_Id) # 499