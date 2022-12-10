"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл."""

dictan = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('NambersR.txt', 'w', encoding='utf-8') as file_21:
    with open('Nambers.txt', 'r', encoding='utf-8') as file_1:
        for el in file_1:
            str_f = el.split(" ")
            str_f[0] = dictan.get(str_f[0])
            print(" ".join(map(str, str_f)))
            file_21.writelines(" ".join(map(str, str_f)))
