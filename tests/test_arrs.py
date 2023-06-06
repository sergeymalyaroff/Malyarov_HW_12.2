import unittest
from utils import arrs



class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], 0, "test"), "test")

    def test_my_slice(self):
        # Тест для нормальной ситуации со срезом от одного элемента до другого
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])

        # Тест для ситуации со срезом всего массива
        self.assertEqual(my_slice([1, 2, 3, 4]), [1, 2, 3, 4])

        # Тест для ситуации, когда начало среза больше длины массива
        self.assertEqual(my_slice([1, 2, 3, 4], 5), [])

        # Тест для ситуации, когда начало среза отрицательное
        self.assertEqual(my_slice([1, 2, 3, 4], -2), [3, 4])

        # Тест для ситуации, когда начало и конец среза отрицательные
        self.assertEqual(my_slice([1, 2, 3, 4], -3, -1), [2, 3])

if __name__ == '__main__':
    unittest.main()




class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
