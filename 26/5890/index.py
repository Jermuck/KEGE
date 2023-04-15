with open("26_5890.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines()));
points.sort(reverse=True);
arr = [];
indexes = [];
while len(indexes) != len(points):
    s = [];
    for x in range(N):
        if sum(s) + points[x] <= LIM and x not in indexes:
            s.append(points[x]);
            indexes.append(x);
    arr.append(s);
print(len(arr), sum(arr[-2])) # 38 1481