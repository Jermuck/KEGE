with open("27A_6318.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines()));
mx = 0;
for x in range(N):
    s = 0;
    for y in range(N):
        if abs(x - y) <= LIM:
            s += points[y];
    mx = max(mx, s);
print(mx) # 81162