with open("27_B.txt") as f:
    LIM = int(f.readline());
    N = int(f.readline());
    nums = list(map(int, f.readlines()));
mx = 0;
for x in range(N):
    for y in range(x + LIM + 1, N):
        mx = max(mx, nums[x] + nums[y]);
print(mx) # 19974