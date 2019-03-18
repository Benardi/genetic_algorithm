import unittest

from genetic_algorithm.dummy_code import dummy_func


class TestEquationSolution(unittest.TestCase):

    def test_dummy(self):

        assert not dummy_func(1, 2)


if __name__ == '__main__':
    unittest.main()
