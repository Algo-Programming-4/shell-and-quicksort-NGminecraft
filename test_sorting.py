import sorting
import random
import unittest


nums = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
sorted_nums = sorted(nums)

class test_sorting(unittest.TestCase):
    def test_bubble(self):
        print(nums)
        result = sorting.bubble(nums)
        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_nums)
            
    def test_selection(self):
        result = sorting.selection(nums)
        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_nums)
            
    def test_insertion(self):
        result = sorting.insertion(nums)
        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_nums)
        
    def test_shell(self):
        result = sorting.shell(nums)
        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_nums)
        
    def test_quicksort(self):
        result = sorting.quicksort(nums)
        self.assertIsNotNone(result)
        self.assertEqual(result, sorted_nums)