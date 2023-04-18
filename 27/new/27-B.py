with open("27B.txt") as f:
    N, LIM = map(int, f.readline().split());
    nums = list(map(int, f.readlines()));
nums *= 2
first = sum(nums[:LIM * 2 + 1]);
mx = first
for x in range(1, N * 2 - (LIM * 2)):
    first = first - nums[x-1] + nums[x + LIM * 2];
    mx = max(first, mx);
print(mx) # 1782723