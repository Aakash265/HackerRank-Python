x = int(input())
y = int(input())
z = int(input())
n = int(input())

List1 = []
List2 = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if((i+j+k) != n):
                List1 = [i,j,k]
                List2.append(List1)

print(List2)