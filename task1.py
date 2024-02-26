'''
Программа выводит все песни которые вышли раньше 01.01.2002.
Данные выводятся в формате "<название песни>-<артист>-<кол-во прослушиваний>.
songs_data - переменная для хранения информации из csv файла
item - один ряд из таблицы
'''

from csv import reader

with open('/home/student/songs.csv') as data_file:
    songs_data=reader(data_file, delimiter = ';')
    for item in songs_data:
        if item[0]=='0':
            item[0]=int(abs(((13-(int(item[3][:2])))+5-int(item[3][3:5])+2023-int(item[3][-4:]))/(int(len(item[1])+int(len(item[2])))))*10000)
        if item[3][-4:] =='date':
            continue
        else:
            if int(item[3][-4:]) >=2002:
                print("'",item[2],item[1],item[0],"'")