import os

def create_forlders(n):
    for i in range(1, n+1):
        folder_name = 'folder_{:02}'.format(i)
        os.mkdir(folder_name)

def delete_forlders(n):
    for i in range(1, n+1):
        folder_name = 'folder_{:02}'.format(i)
        os.rmdir(folder_name)


if __name__ == '__main__':
    create_forlders(9)
    delete_forlders(9)