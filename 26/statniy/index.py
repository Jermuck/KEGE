with open("26.txt") as f:
    LIM, N = map(int, f.readline().split());
    points = []
    for _ in range(N):
        a, b = map(int, f.readline().split());
        points += [(a, b)];
