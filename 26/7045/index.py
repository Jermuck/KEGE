with open("26_7045.txt") as f:
    N, LIM = map(int, f.readline().split());
    marks = [];
    for _ in range(N):
        line = map(int, f.readline().split());
        line = [* line];
        balls = line[1] + line[2] + max(line[3:]);
        marks.append((line[0], balls));
# 222 - with docs / 
marks.sort(reverse=True);
newMarks = [x[1] for x in marks];
newMarks.sort(reverse=True);
arr = []
for x in range(N):
    if len(arr) != LIM and marks[x][0] == 1:
        arr.append(marks[x]);
print(arr)
arr_1 = [];
for x in range(N):
    if len(arr_1) != LIM:
        arr_1.append(newMarks[x]);
print(arr_1[-1])