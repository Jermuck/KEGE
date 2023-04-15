with open("27B_6320.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines())) * 2;
pre_sum = sum(points[0:2 * LIM + 1]);
mx = pre_sum;
for x in range(LIM + 1, 2 * N - LIM):
    pre_sum = pre_sum - points[x - LIM - 1] + points[x + LIM];
    mx = max(pre_sum, mx)
print(mx) # 1782723