with open("27B_6318.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines()));
pre_sum = mx = sum(points[:2 * LIM + 1]);
for y in range(LIM + 1, N - LIM):
    pre_sum = pre_sum - points[y - LIM - 1] + points[y + LIM];
    mx = max(pre_sum, mx);
print(mx) # 641474