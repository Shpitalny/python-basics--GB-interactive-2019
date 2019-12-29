import os
import shutil
import datetime as dt


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def change_dir(name):
    try:
        if os.path.isdir(name):
            os.chdir(name)
        else:
            print('Указанная папка не существует')
    except:
        print('Введен некорректный путь к папке')


def get_list(folders_only=False):
    path = os.getcwd()
    result = os.listdir(path)
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(f'Директория:\n{path}')
    print(f'Состав:\n{result}')


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = dt.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    pass
