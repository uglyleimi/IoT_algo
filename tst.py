import unittest
from unittest.mock import patch
import io


from lab6 import UnionFind, main

class TestLab6(unittest.TestCase):

    def test_union_find_basic(self):

        uf = UnionFind(10)
        uf.union(1, 2)
        uf.union(2, 3)

        self.assertEqual(uf.find(1), uf.find(3))
        self.assertNotEqual(uf.find(1), uf.find(4))


    @patch('builtins.input', side_effect=['1', '1 2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_pair(self, mock_stdout, mock_input):

        main()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[-1], '0')

    @patch('builtins.input', side_effect=['2', '1 2', '3 4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_two_disjoint_pairs(self, mock_stdout, mock_input):

        main()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[-1], '2')

    @patch('builtins.input', side_effect=['2', '1 3', '2 4'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_separated_genders(self, mock_stdout, mock_input):

        main()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[-1], '4')

    @patch('builtins.input', side_effect=['3', '1 2', '2 3', '4 5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mixed_tribes(self, mock_stdout, mock_input):

        main()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[-1], '3')

    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zero_pairs(self, mock_stdout, mock_input):

        main()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output[-1], '0')

if __name__ == '__main__':
    unittest.main()