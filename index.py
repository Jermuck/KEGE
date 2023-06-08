with open('26.txt') as f:
    n = int(f.readline());
    k = int(f.readline());
    l = int(f.readline())
    arr = list(map(int, f.readlines()));
arr.sort(reverse=True);
kameras = [];
indexes = [];
t = 0;
while len(kameras) != k and len(indexes) != n:
    s = [];
    for x in range(n):
        if x not in indexes and sum(s) + arr[x] <= l:
            s.append(arr[x]);
            indexes.append(x);
    kameras.append(s);
    if len(s) != 0:
        t = len(kameras);
print(t)
