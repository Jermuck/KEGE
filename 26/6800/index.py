with open("26_6800.txt") as f:
    N = int(f.readline());
    LIMIT = 100000;
    buys = list(map(int, f.readlines()));
buys.sort();
print(len(buys) // 6) 