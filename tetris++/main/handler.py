import os
import time
from game import create_field

class MainOutput:
    def print_line(self, message):
        print(message)

    def print_game_res(self, arr):
        counter = 0
        for i in arr:
            os.system('clear')
            self.print_line(f'Step: {counter}')
            self.print_line(i)
            counter = counter + 1
            time.sleep(0.5)

class FileSystem:
    def is_exist(self, path):
        return os.path.exists(path)

    def read_file(self, path):
        f = open(path, 'r')
        data = f.read()
        f.close()
        return data

def main_handler(argv, output, fs):
    if len(argv) < 2:
        output.print_line('Please specify input file path')
        return

    if not fs.is_exist(argv[1]):
        output.print_line('File does not exist')
        return

    data = fs.read_file(argv[1])

    if data == None:
        output.print_line('Error while parsing input file')
        return

    game_field = create_field(data)
    game_field.play()

    if len(argv) > 2 and argv[2] == 'full':
        output.print_game_res(game_field.hist)
        return

    output.print_line(game_field.get_field())
    