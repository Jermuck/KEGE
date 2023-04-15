with open('26_5679.txt') as f:
    N, LIM = map(int, f.readline().split());
    points = [];
    for _ in range(N):
        Id, price, cat = f.readline().split();
        if "C" in cat:
            sale = (int(Id) % 100) / 100;
            prc = int(price) - int(price) * sale;
        else:
            prc = int(price);
        points.append((prc, cat));
points.sort();
res = [points[0]];
for y in range(1, N):
    summ = sum(x[0] for x in res);
    if summ + points[y][0] <= LIM:
        res.append(points[y]);
summ = round(sum(x[0] for x in res));
print(summ) # 148922
mx_with_sale = max(x[0] for x in res if "C" in x[1]);
res_2 = max(x[0] for x in points if "C" in x[1] and summ - mx_with_sale + x[0] <= LIM);
print(round(res_2)) # 5073
