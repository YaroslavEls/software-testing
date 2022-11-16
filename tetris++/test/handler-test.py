import unittest
from unittest.mock import Mock
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'main'))
from handler import *


output_mock = Mock()
file_system_mock = Mock()


class TestHandler(unittest.TestCase):
    def setUp(self):
        output_mock.reset_mock()
        file_system_mock.reset_mock()

    def test_no_input_specified(self):
        main_handler([''], output_mock, file_system_mock)

        output_mock.print_line.assert_called_once_with('Please specify input file path')
        output_mock.print_game_res.assert_not_called()
        file_system_mock.is_exist.assert_not_called()
        file_system_mock.read_file.assert_not_called()

    def test_file_not_exist(self):
        file_system_mock = Mock()
        file_system_mock.is_exist.return_value = False
       
        main_handler(['', 'input.txt'], output_mock, file_system_mock)

        output_mock.print_line.assert_called_once_with('File does not exist')
        output_mock.print_game_res.assert_not_called()
        file_system_mock.is_exist.assert_called_once_with('input.txt')
        file_system_mock.read_file.assert_not_called()

    def test_error_while_parsing_file(self):
        file_system_mock = Mock()
        file_system_mock.is_exist.return_value = True
        file_system_mock.read_file.return_value = None

        main_handler(['', 'input.txt'], output_mock, file_system_mock)

        output_mock.print_line.assert_called_once_with('Error while parsing input file')
        output_mock.print_game_res.assert_not_called()
        file_system_mock.is_exist.assert_called_once_with('input.txt')
        file_system_mock.read_file.assert_called_once_with('input.txt')

    def test_final_result(self):
        file_system_mock = Mock()
        file_system_mock.is_exist.return_value = True
        file_system_mock.read_file.return_value = '7 8\n..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####'

        main_handler(['', 'input.txt'], output_mock, file_system_mock)
        
        output_mock.print_line.assert_called_once_with('........\n........\n..p.....\n.ppp....\n..p#....\n...#...#\n#..#####')
        output_mock.print_game_res.assert_not_called()
        file_system_mock.is_exist.assert_called_once_with('input.txt')
        file_system_mock.read_file.assert_called_once_with('input.txt')

    def test_final_result_with_full(self):
        file_system_mock = Mock()
        file_system_mock.is_exist.return_value = True
        file_system_mock.read_file.return_value = '7 8\n..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####'

        main_handler(['', 'input.txt', 'full'], output_mock, file_system_mock)
        
        exp_arg = [
            '..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####',
            '........\n..p.....\n.ppp....\n..p.....\n...#....\n...#...#\n#..#####',
            '........\n........\n..p.....\n.ppp....\n..p#....\n...#...#\n#..#####'
        ]

        output_mock.print_line.assert_not_called()
        output_mock.print_game_res.assert_called_once_with(exp_arg)
        file_system_mock.is_exist.assert_called_once_with('input.txt')
        file_system_mock.read_file.assert_called_once_with('input.txt')


unittest.main()