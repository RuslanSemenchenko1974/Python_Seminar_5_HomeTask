"""Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
 выводить ее на экран."""
import random


def function():
    while True:
        try:
            x = int(input())
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


print('Введите количество цифр : ')

qty_nambers = function()

with open('Namb_Task_5.txt', 'w', encoding='utf-8') as file_n:
    for i in range(qty_nambers):
        file_n.write(str(random.randint(0, 100)) + " ")
with open('Namb_Task_5.txt', 'r', encoding='utf-8') as file_n:
    content = file_n.read()
    lst = content.split(' ')
print(lst)
summ = 0
for el in lst:
    try:
        summ += int(el)
    except ValueError:
        summ += 0
print(f'Сумма чисел в файле Namb_Task_5.txt = {summ}')
