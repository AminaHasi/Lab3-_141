# Гасимова Аміна 141 група
# Лабораторна робота 3
# Дано ціле число N (> 0). Знайти значення виразу 1.1 - 1.2 + 1.3 - ... (N доданків, знаки
# чергуються). Умовний оператор не використовувати

n = int(input("Введіть ціле число N: "))
i = 0
k = 1
val = 1.1
rez = 0
for i in range(1, n+1):
    rez = rez + k * val
    k *= -1
    val += 0.1
print("Результат: ", rez)
