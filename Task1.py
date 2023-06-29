from typing import Generator

# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

addr = r'C:\Geek\file1.txt'

def split_path(addr1: str) -> tuple():
    list_addr1 = addr1.split('\\')
    elements = list_addr1[-1].split('.')
    file_path = '\\'.join(list_addr1[0:-1])
    file_name = elements[0]
    file_expansion = elements[1]
    return file_path, file_name, file_expansion


print(split_path(addr))
