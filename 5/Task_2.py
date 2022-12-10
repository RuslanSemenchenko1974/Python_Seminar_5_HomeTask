"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
us_text = ' '
print('Введите текст построчно, конец ввода "ENTER" : ')
with open('File.txt', 'a', encoding='utf-8') as file_1:
    while us_text != '':
        us_text = input()
        if us_text!='':
            file_1.writelines('\n'+us_text)
    print('Ввод закончен')
with open('File.txt', 'r', encoding='utf-8') as file_1:
    i=0
    str = []
    for el in file_1:
        j = 0
        str = el.split(" ")
        for el2 in str:
            if el2!=''and el2!='\n':
                j+=1
        print(f'Количество слов в {i+1} строке : {j}')
        i+=1
print(f'Количество строк в файле : {i}')
