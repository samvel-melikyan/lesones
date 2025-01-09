print(list(range(5)))
print(list(range(1,10,2)))
print(list(range(10,0,-1)))
print(list(range(0,10,1)))

print("А чтобы подсчитать общее число итераций, нужно умножить количество итераций \nпервого цикла на количество итераций второго: 5*3 = 15 итераций в данном цикле.")

for i in range(5):
    print()
    for j in range(3):
        print(f'i = {i}, j = {j}')



print("----------HW--------------------------")

for i in range(1,11,1):
    print(f"------- {i} ------")
    for j in range(1,11,1):
        print(f'{i} * {j} = {i * j}')


print("----------HW--------------------------")
multiple = 1
for i in range(1,11):
    if i % 2 == 0:
        continue
    multiple *= i
print(multiple)


