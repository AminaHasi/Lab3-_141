#Гасимова Аміна 141 група
#Лабораторна робота 3
#Підрахувати k - кількість тризначних натуральних чисел, сума цифр яких дорівнює n (1≤n≤27).
#Операції ділення не використовувати


print("start")
i = 0
for i in range(100,999):
    num_i = str(i)
    if num_i[0]+num_i[1]+num_i[2] in range(1,28):
        i+=1
print(i)
