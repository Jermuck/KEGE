with open("test.txt") as f:
    N, LIM = map(int, f.readline().split());
    points = list(map(int, f.readlines()));
indexes = [];
arr = []
# Поиск первой разницы обьема и лимита до очитски кеша - 221
#while len(indexes) != len(points):
 #   for x in range(N):
  #      if sum(arr) + points[x] <= LIM and x not in indexes:
   #         arr.append(points[x]);
    #        indexes.append(x);
     #   else:
      #      print(LIM - sum(arr));
       #     break;

while len(indexes) != len(points):
    print(arr)
    for x in range(N):
        if sum(arr) + points[x] <= LIM and x not in indexes:
            arr.append(points[x]);
            indexes.append(x);
        else:
            if len(arr) != 0:
                try:
                    del_file = min(u for u in arr if u >= points[x]);
                    idx = arr.index(del_file);
                    arr.pop(idx)
                except:
                    idx = arr.index(max(arr))
                    arr.pop(idx);
                break;
print(len(arr))