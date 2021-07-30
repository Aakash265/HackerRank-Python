n = int(input())
List1 = []

for i in range (0, n):
    var = int(input())
    List1.append(var)

List2 = []

for i in List1:
    if i not in List2:
        List2.append(i)

List2.sort()
num = len(List2)
print(List2[num-2])