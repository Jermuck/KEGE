with open("26_4684.txt") as f:
    n = int(f.readline());
    prices = list(map(int, f.readlines()));
k = 1666;
prices.sort(reverse=True);
newArr = sum(prices[:1666]) // 2;
print(sum(prices) - newArr) # 49699604 выгодно для автомата