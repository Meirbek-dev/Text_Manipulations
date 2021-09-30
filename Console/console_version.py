#!/usr/bin/env python3
# coding=utf-8

# Сделать консольную программу, которая загружает текст из
# файла, осуществляет заданный вариантом алгоритм и выводит
# полученный результат на экран.

# Текст записан одной длинной строкой.
# Признаком красной строки служит символ $.
# Переформатировать текст в 60-символьные строки, формируя абзацы

def main():
    source_text = open(u'source_text.txt', 'r+').read()
    edited_text = open(u'edited_text.txt', 'w')
    new_list = []
    print("Исходный текст:\n", source_text, "\n")
    for i, symbol in enumerate(source_text):
        if i % 60 == 0:
            new_list += '\n$'
        new_list += symbol
    new_list = ''.join(new_list[1:])
    print("Обработанный текст:\n", new_list)
    edited_text.write(new_list)


if __name__ == '__main__':
    main()
