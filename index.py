with open("26.txt") as f:
    K = int(f.readline());
    N = int(f.readline());
    arr = [];
    for _ in range(N):
        x, y = map(int, f.readline().split());
        arr.append((x, x + y));
arr.sort();
kamera = [(0, 0)] * K;
time = 0
k = 0;
for x in range(len(arr)):
    for j in range(K):
        if kamera[j][1] < arr[x][0]:
            kamera[j] = (0, 0);
    free = [z for z in range(K) if kamera[z] == (0, 0)];
    if len(free) > 0:
        mn = min(free);
        k += 1;
        time += arr[x][1] - arr[x][0]
        kamera[mn] = arr[x];
print(N - k, time)
