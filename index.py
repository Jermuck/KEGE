s = open("24.txt").readline();
mx = 0
for x in 0, 1, 2:
    k = 0;
    for y in range(x, len(s) - 2, 3):
        if s[y] in "81" and s[y+1] in "81" and s[y+2] in "DR":
            k += 1;
        else:
            mx = max(mx, k);
            k = 0;
print(mx)