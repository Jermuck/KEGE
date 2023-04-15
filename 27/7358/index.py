from math import gcd
with open("test.txt") as f:
    n = int(f.readline());
    nums = list(map(int, f.readlines()));
mx_del = 0
mx = 0
for x in range(n):
    arr = [nums[x]]
    for y in range(x + 1, n):
        if gcd(*(arr + [nums[y]])) > mx_del:
            arr.append(nums[y]);
            mx = sum(arr);
        else:
            break;
print(mx)