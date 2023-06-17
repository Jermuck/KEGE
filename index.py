with open('26_8432.txt') as f:
    n = int(f.readline());
    arr = [];
    for _ in range(n):
        x, y, z = f.readline().split();
        arr.append((int(x), int(x) + int(y), z));
avto = [0] * 70;
bus = [0] * 30;
arr.sort()
count = 0;
k_obj = 0;
for st, end, tp in arr:
    flag = False;
    if tp == "A":
        for j in range(70):
            if avto[j] <= st:
                avto[j] = end;
                flag = True;
                k_obj += 1;
                break;
    if tp == "B":
        for j in range(30):
            if bus[j] <= st:
                bus[j] = end;
                flag = True;
                count += 1;
                k_obj += 1;
                break;
    if flag == False and tp =="A":
        for j in range(30):
            if bus[j] <= st:
                bus[j] = end;
                flag = True;
                k_obj += 1;
                break;
print(count, n - k_obj);
