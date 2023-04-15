with open("26_7014.txt") as f:
    N = int(f.readline());
    nums = list(map(int, f.readlines()));
s = 0
res_mx = 0;
while len(nums) != 0:
    mx = max(nums);
    mx_index = max(z for z in range(len(nums)) if nums[z] == mx);
    val = mx * (mx_index + 1)
    s += val
    res_mx = max(res_mx, val)
    nums = nums[mx_index+1:];
print(s, res_mx) # 2496457 2133000