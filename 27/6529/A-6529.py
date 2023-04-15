with open("27A_6529.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines()));
mx = 0;
for x in range(N):
    arr = [points[x]]
    for y in range(x + 1, N):
        arr.append(points[y])
        if sum(arr) <= LIM:
            mx = max(mx, len(arr));
        else:
            break;
print(mx) # 288
