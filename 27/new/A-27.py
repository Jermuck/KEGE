with open("27A.txt") as f:
    N, LIM = map(int, f.readline().split());
    nums = list(map(int, f.readlines()));
mx = 0;
for x in range(N):
    s = 0
    for y in range(N):
        if min(abs(x - y), N - abs(x - y)) <= LIM:
            s += nums[y];
    mx = max(mx, s);
print(mx) # 91573