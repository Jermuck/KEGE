with open("27_B_6057.txt") as f:
    N = int(f.readline());
    nums = [];
    for _ in range(N):
        line = sorted([* map(int, f.readline().split())]);
        nums.append(line);
summ = 0;
dlim = 10 ** 100
for ln in nums:
    a, b, c = ln;
    summ += c;
    if (c - b) % 91 != 0 and (c - b) <= dlim:
        dlim = c - b;
    elif (c - a) % 91 != 0 and (c - a) <= dlim:
        dlim = c - a;
if summ % 91 == 0:
    summ -= dlim;
print(summ) # A - 754612 B - 6133919380