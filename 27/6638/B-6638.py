with open("27A_6638.txt") as f:
    N = int(f.readline());
    road = [0] * 11_000_000
    for _ in range(N):
        Id, k = map(int, f.readline().split());
        c = k // 100 if k % 100 == 0 else k // 100 + 1;
        road[Id] = c;
print(road)