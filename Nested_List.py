if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    #print(students)
    #second_lowest_score = students[1][1]
    second_lowest_score = sorted(list(set([x[1] for x in students])))[1]
    desired_students = []
    for stu in students:
        if stu[1] == second_lowest_score:
            desired_students.append(stu[0])
    print("\n".join(sorted(desired_students)))











# n = int(input())
# names = []
# marks = []

# for i in range(n):
#     name = input()
#     names.append(name)
#     mark = input()
#     marks.append(mark)

# lst = list(marks)
# maximum1 = max(marks)

# remove_list = []

# for i in range(len(marks)):
#     if (marks[i] == maximum1):
#         remove_list.append(i)

# temp = 0

# for x in remove_list:
#     marks.pop(x)

# print(marks)

# maximum2 = max(marks)

# indices = []

# for i in range(len(lst)):
#     if (lst[i] == maximum2):
#         indices.append(i)

# print(indices)








# n = int(input())
# list1 = []
# marks_list = [] 
# names_list = []

# for i in range (n):
#     name = input()
#     names_list.append(name)
#     marks = int(input())
#     marks_list.append(marks)

# sort_list = []
# sort_list = sorted(marks_list)

# var = sort_list[1]

# index = marks_list.index(var)

# print(names_list[index])

