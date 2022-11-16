import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'main'))
from handler import *

messages = []

output_mock = MainOutput()
output_mock.print_line = lambda mes: messages.append(mes)

file_system_mock = FileSystem()
file_system_mock.is_exist = lambda path: Exception('is_exist has been called unexpectedly')
file_system_mock.read_file = lambda path: Exception('read_file has been called unexpectedly')


class TestHandler(unittest.TestCase):
    def setUp(self):
        messages.clear()

    def test_no_input_specified(self):
        main_handler([''], output_mock, file_system_mock)

        self.assertEqual(1, len(messages))
        self.assertEqual('Please specify input file path', messages[0])

    def test_file_not_exist(self):
        file_system_mock = FileSystem()
        file_system_mock.is_exist = lambda path: False
        file_system_mock.read_file = lambda path: Exception('read_file has been called unexpectedly')

        main_handler(['', 'input.txt'], output_mock, file_system_mock)

        self.assertEqual(1, len(messages))
        self.assertEqual('File does not exist', messages[0])

    def test_error_while_parsing_file(self):
        file_system_mock = FileSystem()
        file_system_mock.is_exist = lambda path: True
        file_system_mock.read_file = lambda path: None

        main_handler(['', 'input.txt'], output_mock, file_system_mock)

        self.assertEqual(1, len(messages))
        self.assertEqual('Error while parsing input file', messages[0])

    def test_final_result(self):
        file_system_mock = FileSystem()
        file_system_mock.is_exist = lambda path: True
        file_system_mock.read_file = lambda path: '7 8\n..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####'

        main_handler(['', 'input.txt'], output_mock, file_system_mock)
        
        self.assertEqual(1, len(messages))
        self.assertEqual('........\n........\n..p.....\n.ppp....\n..p#....\n...#...#\n#..#####', messages[0])


unittest.main()