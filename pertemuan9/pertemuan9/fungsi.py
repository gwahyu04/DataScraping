import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def write_to_file(path, data):
    with open(path,'a') as file:
        file.write(data + '\n')

def read_data(path, limit):
    with open(path,'rt') as file:
        count = 0
        for line in file:
            if count == limit:
                break
            if line == "\n":
                continue
            else:
                count += 1
                print(line.replace("\n",""))

def does_file_exist(path):
    return os.path.isfile(path)

def remove_file(path):
    if does_file_exist(path):
        os.remove(path)