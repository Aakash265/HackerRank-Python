<<<<<<< HEAD
n = int(input())
info = {}
marks = []

for i in range (n):
    marks = list(input().split())
    name = marks[0]
    marks.pop(0)
    info[name] = marks

query_name = input()

lst = info.get(query_name)

lst = [float(i) for i in lst]

add = sum(lst)
avg = add/3
avg = "{:.2f}".format(avg)
print(avg)
=======
n = int(input())
info = {}
marks = []

for i in range (n):
    marks = list(input().split())
    name = marks[0]
    marks.pop(0)
    info[name] = marks

query_name = input()

lst = info.get(query_name)

lst = [float(i) for i in lst]

add = sum(lst)
avg = add/3
avg = "{:.2f}".format(avg)
print(avg)
>>>>>>> 397428cf79d51595b0a1e99511e1d408b8aabd6e
