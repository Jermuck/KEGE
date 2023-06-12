import math
with open('26.txt') as f:
    n = int(f.readline());
    k = int(f.readline());
    price = int(f.readline());
    arr = [];
    for _ in range(n):
        x, y, m = map(int, f.readline().split());
        arr.append((x, y, m));
kamera_1 = [0] * k
kamera_2 = [0] * k
kamera_3 = [0] * k
money = 0;
count = 0;
arr.sort()
for client in arr:
    tLevel = client[2];
    time = math.ceil((client[1] - client[0]) / 60 / 60);
    if tLevel == 1:
        for j in range(k):
            if kamera_1[j] <= client[0]:
                kamera_1[j] = client[1] + 60;
                count += 1;
                money += time * price * 1;
                break;
    if tLevel == 2:
        for j in range(k):
            if kamera_2[j] <= client[0]:
                kamera_2[j] = client[1] + 60;
                count += 1;
                money += time * price * 2;
                break;
    if tLevel == 3:
        for j in range(k):
            if kamera_3[j] <= client[0]:
                kamera_3[j] = client[1] + 60;
                count += 1;
                money += time * price * 4
                break;
print(count, money)
