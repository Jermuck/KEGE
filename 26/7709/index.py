with open("26_7709.txt") as f:
    k = int(f.readline());
    n = int(f.readline());
    nums = [];
    for _ in range(n):
        x, y, = map(int, f.readline().split());
        nums.append((x, y));
nums = sorted(nums)
kamera = [(0, 0)] * k;
count = 0
for x in range(n):
    for y in range(k):
        if kamera[y][1] < nums[x][0]:
            kamera[y] = (0, 0); 
    free = [z for z in range(k) if kamera[z] == (0, 0)];
    if len(free) > 0:
        kamera[min(free)] = nums[x];
        count += 1;
        last = min(free) + 1;
print(count, last)
