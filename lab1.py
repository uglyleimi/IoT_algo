'''
Дано відсортований масив цілих чисел `nums` за зростанням (від менших до більших
значень). Напишіть функцію, яка повертає новий масив, в якому кожен елемент є
квадратом відповідного елемента з масиву `nums`. Отриманий масив також повинен бути
відсортованим за зростанням.

Поверніть новий масив відповідно до вхідних даних.
Вхідні дані: nums = [-4,-2,0,1,3]
Результат: [0,1,4,9,16]
Вхідні дані: nums = [1,2,3,4,5]
Результат: [1,4,9,16,25]

'''

import unittest
#тут до квадратів пілносимо
def sorted_squares(nums):
    result = []
    for i in range (len(nums)):
        result.append(nums[i]*nums[i])
        
#баблсорт
    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j] > result[j+1]:
                temp = result[j]
                result[j] = result[j+1]
                result[j+1] = temp
    return result
#тестировоочка
class TestSortedSquares(unittest.TestCase):
    def test_sorted_squares(self):
        self.assertEqual(sorted_squares([-4,-2,0,1,3]), [0,1,4,9,16])
        self.assertEqual(sorted_squares([1,2,3,4,5]), [1,4,9,16,25])   
        
if __name__ == '__main__':
    unittest.main()
 
'''
 складність O(n^2)
 можна було через sort тоді б палучилось O(n)
 
'''

    