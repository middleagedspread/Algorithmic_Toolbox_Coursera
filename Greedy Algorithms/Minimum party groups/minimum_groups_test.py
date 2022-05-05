import unittest
from minimum_groups import compute_min_number_of_groups

class minimum_groups(unittest.TestCase):
    def test_something(self):

         for (number_of_children, children_ages, answer) in [
            (6, [5.5, 6.1, 6.4, 6.6, 7.0, 7.2], 2),
            (2, [7.2, 7.6], 1),
            (4, [5.0, 6.1, 7.2, 8.3], 4),
            (5, [5.0, 6.0, 7.0, 8.0, 9.0], 3)
        ]:
            self.assertEqual(compute_min_number_of_groups(number_of_children, children_ages), answer)




if __name__ == '__main__':
    unittest.main()
