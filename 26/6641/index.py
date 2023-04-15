with open("26_6641.txt") as f:
    N, LIM = map(int, f.readline().split());
    nums = [];
    for _ in range(N):
        price, cat = f.readline().split();
        nums += [(int(price), cat)];
nums.sort()
arr = [nums[0]]
for x in range(1, len(nums)):
    if sum([z[0] for z in arr]) + nums[x][0] <= LIM:
        arr.append(nums[x]);
    else:
        index = x;
        break;
ost_nums = nums[index:][:];
ost_nums = [x for x in ost_nums if x[1] == "S"];
indexes = [];
arr = arr[::-1]
k = 0
for x in range(len(arr)):
    if arr[x][1] == "W":
        for z in range(len(ost_nums)):
            s = sum(y[0] for y in arr) - arr[x][0] + ost_nums[z][0];
            if z not in indexes and s <= LIM:
                print(arr[x], ost_nums[z])
                arr[x] = ost_nums[z];
                indexes.append(z);
                k += 1;
            else:
                break