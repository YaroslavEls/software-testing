import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'main'))
from game import *

class TestGame(unittest.TestCase):
    def setUp(self):
        self.data = '7 8\n..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####'
        self.field = create_field(self.data)

    def test_field_size(self):
        self.assertEqual(self.field.rows, 7)
        self.assertEqual(self.field.cols, 8)

    def test_field_land(self):
        expected_coords = [[3, 4], [3, 5], [7, 5], [0, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]]
        counter = 0
        for i in self.field.land:
            self.assertEqual(i.x, expected_coords[counter][0])
            self.assertEqual(i.y, expected_coords[counter][1])
            counter = counter + 1

    def test_field_figure(self):
        expected_coords = [[2, 0], [1, 1], [2, 1], [3, 1], [2, 2]]
        counter = 0
        for i in self.field.fig:
            self.assertEqual(i.x, expected_coords[counter][0])
            self.assertEqual(i.y, expected_coords[counter][1])
            counter = counter + 1

    def test_field_figure_to_check(self):
        expected_coords = [[1, 1], [3, 1], [2, 2]]
        counter = 0
        for i in self.field.fig_to_check:
            self.assertEqual(i.x, expected_coords[counter][0])
            self.assertEqual(i.y, expected_coords[counter][1])
            counter = counter + 1

    def test_field_get_field(self):
        exp = '..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####'
        res = self.field.get_field()
        self.assertEqual(res, exp)

    def test_field_get_dot(self):
        self.assertEqual(self.field.get_dot(2, 0).value, 'p')
        self.assertEqual(self.field.get_dot(3, 1).value, 'p')
        self.assertEqual(self.field.get_dot(1, 3).value, '.')
        self.assertEqual(self.field.get_dot(3, 4).value, '#')
        self.assertEqual(self.field.get_dot(7, 6).value, '#')

    def test_field_step(self):
        self.field.step()
        
        expected_coords = [[2, 1], [1, 2], [2, 2], [3, 2], [2, 3]]
        counter = 0
        for i in self.field.fig:
            self.assertEqual(i.x, expected_coords[counter][0])
            self.assertEqual(i.y, expected_coords[counter][1])
            counter = counter + 1

    def test_field_play(self):
        self.assertEqual(self.field.check(), True)
        self.field.play()
        self.assertEqual(self.field.check(), False)

        expected_coords = [[2, 2], [1, 3], [2, 3], [3, 3], [2, 4]]
        counter = 0
        for i in self.field.fig:
            self.assertEqual(i.x, expected_coords[counter][0])
            self.assertEqual(i.y, expected_coords[counter][1])
            counter = counter + 1

    def test_field_hist(self):
        self.field.play()

        exp = [
            '..p.....\n.ppp....\n..p.....\n........\n...#....\n...#...#\n#..#####',
            '........\n..p.....\n.ppp....\n..p.....\n...#....\n...#...#\n#..#####',
            '........\n........\n..p.....\n.ppp....\n..p#....\n...#...#\n#..#####'
        ]
        res = self.field.hist

        self.assertEqual(res, exp)

    def test_stop_in_the_bottom(self):
        self.data = '5 6\n..p...\n##p.##\n##pp##\n##..##\n##..##'
        self.field = create_field(self.data)

        self.field.play()

        exp = '......\n##..##\n##p.##\n##p.##\n##pp##'
        res = self.field.get_field()
        self.assertEqual(res, exp)


unittest.main()