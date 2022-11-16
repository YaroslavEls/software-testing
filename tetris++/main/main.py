import sys
from handler import *

def main():
    output = MainOutput()
    fs = FileSystem()
    main_handler(sys.argv, output, fs)

if __name__ == '__main__':
    main()