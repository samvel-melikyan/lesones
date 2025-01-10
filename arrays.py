clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert', 'Pam Beesly', 'Kevin Malone']
mix_list = [1, 1.1, True, 'Hello', 'python allows the mixed lists']
print(mix_list)
print(mix_list[4])
print(mix_list[1], " | with using negative indexing")
mix_list[3] = "new value!".upper()
print(mix_list)
print()
print("=========Срезы=========================")
print("Если вам понадобится, например, вывести каждый второй элемент списка, то такую задачу можно решить не перебором индексов, а с помощью срезов.")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("|-",numbers[:], "\n|_numbers[:] : # срез всего списка ; # start=0 stop=10 step=1")
print("|-",numbers[:5], "\n|_numbers[:5] : # срез c нулевого по пятый элемент списка ; # start=0 stop=5 step=1")
print("|-",numbers[1:], "\n|_numbers[1:] : # срез c первого по последний элемент списка ; # start=1 stop=10 step")
print("|-",numbers[3:6], "\n|_numbers[3:6] : # срез с третьего по шестой элемент списка ; # start=3 stop=6 step=1")
print("|-",numbers[1::2], "\n|_numbers[1::2] : # каждый второй элемент списка (четные индексы) ; # start=1 stop=10 step=2")
print()
print("=========BAsic array methods=========================")
print("==========append()++++++++++++")
clients = ['Michael Scott', 'Dwight Schrute', 'Jim Halpert',
        'Pam Beesly', 'Kevin Malone']

# выведем исходный список
print(clients)

# добавим новый элемент в список
clients.append('Oscar Martinez')

# выведем получившийся список
print(clients)
print(len(clients))
# считаем имя клиента с консоли
# new_client = input('Введите имя клиента: ') #-----------------------------
# добавим этого клиента в список
# clients.append(new_client) #-----------------------------

# выведем итоговый список
print(clients)
print(len(clients))

for i in range(len(clients)): # i = [0, 1, 2, 3, 4]
    print(f'{i+1}. {clients[i]}')

print("---------HW----------------")
coworkers = ['Piter', 'James', 'Souy', 'Nataly', 'Maourineo']
new_coworker = input("                type a name: ")
if new_coworker in coworkers:
    print("HE/SHE is already in the coworker list!")
else:
    coworkers.append(new_coworker)
    if new_coworker in coworkers:
        print("HE/SHE added to coworker lsit successfully!")
    else:
        print("I think we have an issue, we'll fix it don't worry ;), but also don't worry, because this part will not be executed :D")
print(f"The first coworkers is` {coworkers[1]}\nThe last is` {coworkers[-1]}")
print(f"Every each coworker: {list(coworkers[::1])} \nEvery second coworker: {list(coworkers[::2])}")
print(f"I have {len(coworkers)} coworkers")






















































