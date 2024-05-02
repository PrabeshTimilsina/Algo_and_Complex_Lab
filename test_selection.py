import unittest
from selection import selection_sort

class TestInsertion(unittest.TestCase):

    def test_selection(self):
        input_data=[3,1,2,5]
        result= selection_sort(input_data)
        self.assertEqual(result, [1,2,3,5])

if __name__ == "__main__":
    unittest.main()