with open('26_8482.txt') as f:
    n = int(f.readline());
    k = int(f.readline());
    arr = [];
    for _ in range(n):
        x, y = map(int, f.readline().split());
        arr.append((x, y))
arr.sort();
places = [0] * k
count = 0;
idx = 0;
for client in arr:
    flag = False;
    for j in range(k):
        if client[0] > places[j]:
            places[j] = client[1] + 5;
            flag = True;
            count += 1;
            idx = j + 1;
            break;
    if not flag:
        mn = min(places);
        freeTime = mn - client[0] + 1;
        if freeTime <= 10:
            T = client[1] - client[0];
            index = places.index(mn);
            if places[index] + T + 1 <= 1380:
                places[index] += 1 + 5 + T;
                count += 1;
                idx = index + 1;
print(count, idx)

