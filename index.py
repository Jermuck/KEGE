arr = [];
alf = "ГЕЭ023";
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            arr += [x1 + x2 + x3 + x4 + x5 + x6 + x7];
first = [x for x in range(len(arr)) if arr[x] == "ЕГЭ2023"];
second = [x for x in range(len(arr)) if arr[x] == "2023ЕГЭ"]
print(second[0] - first[0] - 1)