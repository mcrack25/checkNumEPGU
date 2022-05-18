import datetime
from packages.connection import *
from app.models.WhatTable import WhatTable
from app.models.WhereTable import WhereTable
from app.controllers.WhatUploader import WhatUploader
from app.controllers.WhereUploader import WhereUploader
from app.controllers.WhatController import WhatController
from app.controllers.WhereController import WhereController
from app.controllers.ResultFile import ResultFile

def showTime():
    now = datetime.datetime.now()
    result = now.strftime("%d.%m.%Y %H:%M:%S")
    return result

def showInfo(text):
    result = showTime() + ' - ' + text
    return result

def printInfo(text):
    info_text = showInfo(text)
    print(info_text)

if(__name__ == "__main__"):
    printInfo('Программа запущена!!!')
    try:
        db.connect()

        # Удаляем таблицы, если вдруг решили поменять структуру БД
        WhatTable.drop_table()
        WhereTable.drop_table()
        # Удаляем таблицы, если вдруг решили поменять структуру БД

        # Создаём таблицы
        WhatTable.create_table()
        WhereTable.create_table()
        # Создаём таблицы

        # Очищаем таблицы
        WhatTable.truncate_table()
        WhereTable.truncate_table()
        # Очищаем таблицы
    except:
        printInfo('Ошибка!!! Не удалось подключиться к базе данных!')
        exit()

    # Загружаем данные в базу
    printInfo('Данные из xlsx таблиц загружаются в базу')
    WhatUploader().run()
    WhereUploader().run()
    printInfo('Данные из xlsx таблиц успешно загружены')
    # Загружаем данные в базу

    # Создаём объект файла с результатом
    resultObj = ResultFile()
    resultObj.headerContentPut()
    # Создаём объект файла с результатом

    # Вытаскиваем все данные из БД
    what_rows = WhatController().getData()
    count_rows = len(what_rows)
    # Вытаскиваем все данные из БД

    # Перебираем содержимое БД
    printInfo('Начинаем сравнение таблиц')
    this_row = 1
    for what_row in what_rows:
        printInfo(what_row.file_name + ': Обаботана ' + str(this_row) + ' строка из ' + str(count_rows))
        this_row+=1

        where_has = WhereController().hasSnils(what_row.snils)
        if where_has['status']:
            info = {
                "what_file": what_row.file_name,
                "what_row": what_row.num_row,
                "where_file": where_has['result'].file_name,
                "where_row": where_has['result'].num_row,
                "value": what_row.snils,
                "request_date": what_row.request_date,
                "serviceid": what_row.serviceid
            }
            resultObj.contentRowPut(info)
        else:
            info = {
                "what_file": what_row.file_name,
                "what_row": what_row.num_row,
                "where_file": 'None',
                "where_row": 'None',
                "value": what_row.snils,
                "request_date": what_row.request_date,
                "serviceid": what_row.serviceid
            }
            resultObj.contentRowPut(info)
    printInfo('Сравнение таблиц успешно завершено')

    # Сохраняем файл результата
    printInfo('Сохраняем результа в файл')
    resultObj.saveFile()
    # Сохраняем файл результата

    printInfo('Программа выполнена!!!')
    print('')
    print('***')
    print('Название программы: checkSnils v3.0')
    print('Разработка: Министерства труда и социального развития РД')
    print('Разработчик: Ахмедов Мурад Алилович')
    print('***')
    print('')
    input('Нажмите любую клавишу, для завершения работы программы')