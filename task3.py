'''
Программа выводит название одной песни по запросу пользователя.
Формат вывода : "У <артист> найдена песня: <название песни>".
Artist_name - переменная для хранения имени автора
songs_data - переменная для хранения информации из csv файла
flag - флаг для проверки наличия песен у автора.
'''

from csv import reader

with open('/home/student/songs.csv') as data_file:
    songs_data=reader(data_file, delimiter = ';')
    artist_name=input()
    while artist_name !='0':
            for item in songs_data:
                flag=0
                if item[1] == artist_name:
                    flag=1
                    print("У",artist_name,"найдена песня:",item[2])
                    artist_name=input()
            if artist_name=="0":
                break
            if flag==0:
                print("К сожалению, ничего не удалось найти")
                break
