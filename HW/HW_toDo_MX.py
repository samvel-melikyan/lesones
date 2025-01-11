todo_list = []
for i in range(7):
    todo_list.append(['']*3)
print(todo_list)
for i in range(7):
    for j in range(3):
        todo_list[i][j] = input("type_")
print(todo_list)
