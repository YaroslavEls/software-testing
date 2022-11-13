import sys
from handler import *

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print('Please specify input file path')
        return

    output = MainOutput()
    fs = FileSystem()
    main_handler(file_path, output, fs)

if __name__ == '__main__':
    main()