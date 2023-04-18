print(12341111111 < 10 ** 10);
def findDels(num):
    arr = set();
    for x in range(1, round(num ** 0.5) + 1):
        if num % x == 0:
            arr.add(num // x);
            arr.add(x);
    if len(arr) == 2: return 1;
    return 0;
arr = set()
for x in range(1, 1111111):
    summ = sum(int(z) for z in str(x));
    vuraz = (summ + 2) ** 3
    value = int(f'1234{x}');
    if value <= 10 ** 10 and value % vuraz and findDels(summ):
        arr.add(summ);
print(sorted(arr))