info = '''
Доступные команды консольного файлового менеджера:
    list [folders] - список файлов и папок текущей директории
    chdir <dir> - сменить директорию с текущей на <dir>
    create_file <name.ext> - создание файла с именем <name.ext>
    create_folder <name> - создание папки с именем <name> 
    delete <name> - удаление файла или папки с именем <name>
    copy <name> <new_name> - копирование файла или папки; <name> - текущее имя, <new_name> - новое имя
    game - играть в игру "Угадай число (наоборот)": пользователь загадывает число, а комппьютер пытается уго угадать

'''

import sys
import os
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir
from game_inversed import game_inversed

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Укажите команду в качестве аргумента запускаемого файла')
    print(info)
else:
    if command == 'list':
        get_list()

    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя создаваемого файла вторым аргументом')
        else:
            create_file(name)

    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя создаваемой папки вторым аргументом')
        else:
            create_folder(name)

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя удаляемой папки или файла вторым аргументом')
        else:
            delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Укажите исходное и новое имя файла или папки вторым и третьим аргументами')
        else:
            copy_file(name, new_name)

    elif command == 'chdir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя папки вторым аргументом')
        else:
            change_dir(name)

    elif command == 'game':
        game_inversed()

    elif command == 'help':
        print(info)

save_info('Конец')
