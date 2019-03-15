from .context import genetic_algorithm
from genetic_algorithm.dummy_code import dummy_func

import unittest


class TestEquationSolution(unittest.TestCase):

    def dummy_test(self):
        assert dummy_func() == 2

if __name__ == '__main__':
    unittest.main()

