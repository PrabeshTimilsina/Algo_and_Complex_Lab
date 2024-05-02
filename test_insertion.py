import unittest
from insertion import insertion_sort

class TestInsertion(unittest.TestCase):

    def test_insertion(self):
        input_data=[3,1,2,5]
        result= insertion_sort(input_data)
        self.assertEqual(result, [1,2,3,5])

if __name__ == "__main__":
    unittest.main()