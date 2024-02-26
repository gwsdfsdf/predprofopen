'''
Программа выводит все песни которые вышли раньше 01.01.2002.
Данные выводятся в формате "<название песни>-<артист>-<кол-во прослушиваний>.
songs_data - переменная для хранения информации из csv файла
item - один ряд из таблицы
'''

from csv import reader, writer

rusalph = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
engalph = 'QWERTYUIOPASDFGHJKLZXCVBNM'

with open('/home/student/songs.csv') as data_file:
    songs_data = reader(data_file, delimiter=';')
    russian_artist = []
    english_artist = []
    for item in songs_data:
        if item[1][:1] in rusalph:
            russian_artist.append(item[1])
        else:
            english_artist.append(item[1])
    for artist in russian_artist:
        artist = writer('w', 'russian_artists.txt')
    for engartist in english_artist:
        engartist = writer('w', 'foreign_artists.txt')
