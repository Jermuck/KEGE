with open("27_B_6032(1).txt") as f:
    N = int(f.readline());
    arr = []
    for _ in range(N):
        arr.append(sorted([* map(int, f.readline().split())]));
summ = 0;
dl = 10 ** 20;
for line in arr:
    a, b = line;
    summ += b;
    if (b - a) % 13 != 0 and (b - a) <= dl:
        dl = b - a;
if summ % 13 != 0:
    summ -= dl;
print(summ) # A - 2032472 B - 2012220340