#!/bin/env python3
table = list()
print('Правила ввода данных: если клетка пустая введите 0, если нет - цифру от 1 до 9 таким образом,'
      ' чтобы между цифрами одной строки был пробел. Если вы сразу хотите вставить всю таблицу,'
      ' то вставляйте так, чтобы в конце вашего ввода был переход на новую (десятую) строку,'
      ' в этом случае таблица будет считана корректно.')
print('Пример ввода одной из строк: \n1 2 3 4 6 7 8 9\n')
print('Введите данные для игры: ')
for i in range(1, 10):
    print(f'  Введите данные для {i}-ой строки: ')
    result = input().split(' ')
    if len(result) != 9:
        if len(result) == 10:
            result = result[:-1]
        else:
            print('Неправильный ввод')
            exit(2)
    result = [i for i in result if -1 < int(i) < 10]
    if len(result) == 9:
        table.append(result)
    else:
        print('Неправильный ввод')
        exit(2)
print()

table2 = list()

for i in [0, 3, 6]: # преобразование строк в строки квадратов, каждая строка в списке - следующий квадрат
    for j in [0, 3, 6]:
        line1 = ', '.join(table[i][j:j + 3]) + ', '
        line2 = ', '.join(table[i + 1][j:j + 3]) + ', '
        line3 = ', '.join(table[i + 2][j:j + 3])

        table2.append((line1 + line2 + line3).split(', '))

for i in table2:
    print(i)


def not_filled_check(array): # функция, проверяющая наличие пустых клеток, True - есть пустые клетки, False - их нет
    condition = False
    for i in array:
        for j in i:
            if j == '0':
                condition = True
                break
    return condition


def duplicate(array): # функция, проверяющая наличие повторяющихся элементов в одном квадрате, True - есть, False - нет
    condition = False
    for i in array:
        for j in i:
            if i.count(j) > 1 and j != '0':
                condition = True
                break
    return condition


def squaring(return_array, return2_array, lines_nulling=False):
    return3_array, return4_array = [], []
    line0, line1, line2, line3, line4, line5, line6, line7, line8 = [], [], [], [], [], [], [], [], []
    for i in return_array:
        line0.append(i[0])
        line1.append(i[1])
        line2.append(i[2])
        line3.append(i[3])
        line4.append(i[4])
        line5.append(i[5])
        line6.append(i[6])
        line7.append(i[7])
        line8.append(i[8])
    return2_array.append(line0)
    return2_array.append(line1)
    return2_array.append(line2)
    return2_array.append(line3)
    return2_array.append(line4)
    return2_array.append(line5)
    return2_array.append(line6)
    return2_array.append(line7)
    return2_array.append(line8)
    
    if lines_nulling:
        for i in return2_array:
            i = fill_one(i)
            return4_array.append(i)

    return2_array = return4_array

    for i in range(0, 7, 3): # преобразование строк в строки квадратов, каждая строка в списке - следующий квадрат
        for j in range(0, 7, 3):
            line1 = ', '.join(return2_array[i][j:j + 3]) + ', '
            line2 = ', '.join(return2_array[i + 1][j:j + 3]) + ', '
            line3 = ', '.join(return2_array[i + 2][j:j + 3])

            return3_array.append((line1 + line2 + line3).split(', '))
    return return3_array


def fill_one(array):
    if array.count('0') == 1:
        for i in range(10):
            if str(i) not in array:
                array[array.index('0')] = str(i)
                break
    return array


def one_null(array): # функция, проверяющая, есть ли в строке колонке лишь один пропуск, если он один, то функция заполняет его
    return_array, return2_array = [], []
    prom_string, column_count, num_count = [], 0, 0
    for y in range(9): # проходимся по 9 колонкам
        for i in range(column_count, 9, 3):
            for j in range(num_count, 9, 3):
                prom_string.append(array[i][j])
        prom_string = fill_one(prom_string)
        return_array.append(prom_string.copy())
        prom_string.clear()

        if y == 2:
            column_count = 1
        elif y == 5:
            column_count = 2

        if num_count == 2:
            num_count = 0
        else:
            num_count += 1

    return2_array = squaring(return_array, return2_array, True)

    return return2_array


def square_analysis(array):
    for i in range(8, -1, -1):
        print(f'Проверка квадрата № {i + 1}')
        if array[i].count('0') > 1:
            current_arr, ost, nums = array[i], [], ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # ost - список, хранящий цифры, которые есть в квадрате
            for j in current_arr:
                if j != '0':
                    ost.append(j)
            razn = sorted(list(set(nums) - set(ost))) # razn - список, хранящий разницу между списком nums и ost
            # print(razn)
            to_del = []
            null_index_s = [i for i in range(len(current_arr)) if current_arr[i] == '0'] # список всех вхождений "0" в квадрат
            for j in razn: # элементы, которые можно вставить на место пропуска
                # print(' ', null_index_s)
                pot_pos = [] # список возможных позиций для вставки элемента
                for x in null_index_s: # индекс пропуска
                    if x in [0, 1, 2]:
                        if i in [6, 7, 8]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[6][0:3])
                            row_comparsion.extend(array[7][0:3])
                            row_comparsion.extend(array[8][0:3])

                            spis1 = i - 3
                            spis2 = spis1 - 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x + 3])
                            col_comparsion.append(array[spis1][x + 6])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x + 3])
                            col_comparsion.append(array[spis2][x + 6])
                            
                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                        elif i in [3, 4, 5]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[3][0:3])
                            row_comparsion.extend(array[4][0:3])
                            row_comparsion.extend(array[5][0:3])

                            spis1 = i - 3
                            spis2 = i + 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x + 3])
                            col_comparsion.append(array[spis1][x + 6])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x + 3])
                            col_comparsion.append(array[spis2][x + 6])
                            
                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                        elif i in [0, 1, 2]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[0][0:3])
                            row_comparsion.extend(array[1][0:3])
                            row_comparsion.extend(array[2][0:3])

                            spis1 = i + 3
                            spis2 = spis1 + 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x + 3])
                            col_comparsion.append(array[spis1][x + 6])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x + 3])
                            col_comparsion.append(array[spis2][x + 6])
                            
                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                    elif x in [3, 4, 5]:
                        if i in [6, 7, 8]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[6][3:6])
                            row_comparsion.extend(array[7][3:6])
                            row_comparsion.extend(array[8][3:6])

                            spis1 = i - 3
                            spis2 = spis1 - 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x + 3])
                            col_comparsion.append(array[spis1][x - 3])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x + 3])
                            col_comparsion.append(array[spis2][x - 3])
                            
                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                        elif i in [3, 4, 5]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[3][3:6])
                            row_comparsion.extend(array[4][3:6])
                            row_comparsion.extend(array[5][3:6])

                            spis1 = i - 3
                            spis2 = i + 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x + 3])
                            col_comparsion.append(array[spis1][x - 3])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x + 3])
                            col_comparsion.append(array[spis2][x - 3])
                            
                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                        elif i in [0, 1, 2]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[0][3:6])
                            row_comparsion.extend(array[1][3:6])
                            row_comparsion.extend(array[2][3:6])

                            spis1 = i + 3
                            spis2 = spis1 + 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x + 3])
                            col_comparsion.append(array[spis1][x - 3])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x + 3])
                            col_comparsion.append(array[spis2][x - 3])
                            
                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                    elif x in [6, 7, 8]:
                        if i in [6, 7, 8]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[6][6:9])
                            row_comparsion.extend(array[7][6:9])
                            row_comparsion.extend(array[8][6:9])

                            spis1 = i - 3
                            spis2 = spis1 - 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x - 3])
                            col_comparsion.append(array[spis1][x - 6])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x - 3])
                            col_comparsion.append(array[spis2][x - 6])

                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                        elif i in [3, 4, 5]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[3][6:9])
                            row_comparsion.extend(array[4][6:9])
                            row_comparsion.extend(array[5][6:9])

                            spis1 = i - 3
                            spis2 = i + 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x - 3])
                            col_comparsion.append(array[spis1][x - 6])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x - 3])
                            col_comparsion.append(array[spis2][x - 6])

                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                        elif i in [0, 1, 2]:
                            row_comparsion, col_comparsion = [], []
                            row_comparsion.extend(array[0][6:9])
                            row_comparsion.extend(array[1][6:9])
                            row_comparsion.extend(array[2][6:9])

                            spis1 = i + 3
                            spis2 = spis1 + 3
                            col_comparsion.append(array[spis1][x])
                            col_comparsion.append(array[spis1][x - 3])
                            col_comparsion.append(array[spis1][x - 6])
                            col_comparsion.append(array[spis2][x])
                            col_comparsion.append(array[spis2][x - 3])
                            col_comparsion.append(array[spis2][x - 6])

                            if j not in row_comparsion and j not in col_comparsion:
                                pot_pos.append(x)

                if len(pot_pos) == 1:
                    array[i][pot_pos[0]] = j
                    del null_index_s[null_index_s.index(pot_pos[0])]
                    to_del.append(j)
                
        elif array[i].count('0') == 1:
            array[i] = fill_one(array[i])
        else:
            continue

    return array


def vertical_analysis(array):
    print('Проверка линей по вертикали...')
    return array


if duplicate(table2): # если есть повторяющиеся элементы в квадрате
    print('Таблица введена неправильна: есть повторяющиеся элементы в квадрате')
else:
    print('Ввод правильный')
    while not_filled_check(table2): # цикл не завершается, пока есть пустые клетки в таблице
        table2 = one_null(table2)
        print('Проверка на наличие единственной свободной клетки в строке/столбце/квадрате...')
        table2 = square_analysis(table2)
        print('Анализ квадрата...')
    print("Решенное судоку:")
    for i in range(len(table2)):
        if i == 0 or i == 3 or i == 6:
            line = ' '.join(table2[i][0:3]) + ' ' + ' '.join(table2[i + 1][0:3]) + ' ' + ' '.join(table2[i + 2][0:3])
            print(line)
        elif i == 1 or i == 4 or i == 7:
            line = ' '.join(table2[i - 1][3:6]) + ' ' + ' '.join(table2[i][3:6]) + ' ' + ' '.join(table2[i + 1][3:6])
            print(line)
        elif i == 2 or i == 5 or i == 8:
            line = ' '.join(table2[i - 2][6:9]) + ' ' + ' '.join(table2[i - 1][6:9]) + ' ' + ' '.join(table2[i][6:9])
            print(line)
lol = input() # нужна для того, чтобы программа не закрывалась в консоли
