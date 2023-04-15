with open("test.txt") as f:
    N = int(f.readline());
    points = [0] * 12_000_000;
    for _ in range(N):
        km, k = map(int, f.readline().split());
        c = k // 44 if k % 44 == 0 else k // 44 + 1;
        points[km] = c;
c = 0
for x in range(12_000_000):
    c += points[x] * x;
mn = 10 ** 30
before = points[0];
summ = sum(points);
for x in range(12_000_000):
    c = c + before - (summ - before);
    if points[x] > 0:
        mn = min(mn, c);
    before += points[x];
print(mn)