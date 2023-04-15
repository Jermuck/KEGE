with open("27A_6320.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines()));
mx = 0;
for x in range(N):
    pre_summ = 0;   
    for y in range(N):
        if min(abs(x - y), N - abs(x - y)) <= LIM:
            pre_summ +=  points[y];
    mx = max(mx, pre_summ);
print(mx) # 91573