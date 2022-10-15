# Логгирование операций выполняемых калькулятором
# @made by Sergienko Pavel

from datetime import datetime as dt
from os.path import getsize


def SaveRecordToLogFile(data):
    # ls: список следующих параметров - вид операции, входные параметры, результат.
    # Каждый из этих параметров списка - строка

    # требуемая длина списка параметров
    right_ls_len = 3
    # название файла логгирования logcalc.csv можно добавить в .gitignore
    log_file_Name = 'logcalc.csv'

    # для русско-язычного файла csv в начало файла надо записывать символ unicode - FEFF.
    # Это признак файла UTF-9 with BOM (знака порядка байтов). И тогда при открытии csv в Excel
    # русский текст отобразится корректно.
    # data_header = ['Дата', 'Время', 'Вид операции', 'Входные данные', 'Результат']
    data_header = ['Date', 'Time', 'Type operation', 'Source Data', 'Result']
    data_row = []

    if len(data) != right_ls_len:
        print(f'Количество параметров не равно {right_ls_len}!')
        return False
    try:
        with open(log_file_Name, 'a', encoding='utf-8') as flog:
            if getsize(flog.name) == 0:
                # если файл новый, то пишем специальную последовательность \uFEFF,
                # для автоматического определения Excel типа файла
                # (иначе нужно каждый раз указывать при открытии) и
                # добавляем строку заголовка
                flog.write(str(";".join(data_header) + '\n'))
            # в список добавляем требуемые параметры
            data_row.append(dt.now().strftime('%d.%m.%Y'))
            data_row.append(dt.now().strftime('%H:%M:%S'))
            for cur_param in data:
                if cur_param == '':
                    print(f'Один из параметров строки вход.параметров пустой. Строка: {data}')
                    return False
                data_row.append(cur_param)
            # пишем в лог-файл строку данных
            flog.write(str(";".join(data_row)) + '\n')
    except PermissionError:
        print('Доступ к файлу запрещён (возможно другой программой).')
        return False

    # в случае успешного логгирования записи функция возвращает True,
    # в случае ошибки записи - False (не совпадает количество элементов списка,
    # один из входных параметров списка - пустой.
    return True


# тестирование логгирования
ls = ['+', '2, 5', '10']
Status = SaveRecordToLogFile(ls)

if Status == True:
    print('Логгирование выполнено успешно!')
else:
    print('Логгирование НЕ выполнено!')
