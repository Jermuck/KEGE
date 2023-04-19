with open("test.txt") as f:
    N = int(f.readline());
    nums = list(map(int, f.readlines()));
mx = 0;

for x in range(N):
    for y in range(x + 1, N): 
        pass 