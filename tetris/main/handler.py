import os
from game import create_field

class MainOutput:
    def print_line(self, message):
        print(message)

class FileSystem:
    def is_exist(self, path):
        return os.path.exists(path)

    def read_file(self, path):
        f = open(path, 'r')
        data = f.read()
        f.close()
        return data

def main_handler(file_path, output, fs):
    if not fs.is_exist(file_path):
        output.print_line('File does not exist')
        return

    try:
        data = fs.read_file(file_path)
    except:
        output.print_line('Error while reading the file')
        return

    game_field = create_field(data)
    game_field.play()
    output.print_line(game_field.get_field())