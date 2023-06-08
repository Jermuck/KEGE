with open('26_7826.txt') as f:
    k, n = map(int, f.readline().split())
    arr = [];
    for _ in range(n):
        x, y = map(int, f.readline().split());
        arr.append((x, y));
arr.sort();
people = [0] * n;
atrac = [0] * k;

for x in range(n):
    st, end = arr[x];
    if st == arr[x - 1][0] and people[x - 1] > 0:
        atrac[people[x - 1] - 1] = end;
        people[x] = people[x - 1];
        continue;
    for j in range(k):
        if atrac[j] < st:
            atrac[j] = end;
            people[x] = j + 1;
            break;
print(sum(1 for x in people if x > 0), [x for x in people if x > 0][-1])

