from cgitb import reset
from math import expm1
from unittest import removeResult

import data
import hw1
import unittest

from data import Price, Rectangle, Point, Book, Circle, Employee


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "San Luis Obispo"
        result = hw1.vowel_count(input)
        expected = 6
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "qwertyuiopasdfghjklzxcvbnm"
        result = hw1.vowel_count(input)
        expected = 5
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input =[[1,2],[],[1],[42,2,5,1]]
        result = hw1.short_lists(input)
        expected = [[1,2]]
        self.assertEqual(expected, result)


    def test_short_lists_2(self):
        input = [[4,2, 6], [1,1,4], [], [], [1,2,3,4,5,6,7,8,9,0]]
        result = hw1.short_lists(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[4,3], [1, 9], [], [4,3,2], [0, -1]]
        result = hw1.ascending_pairs(input)
        expected = [[3,4], [1, 9], [], [4,3,2], [-1, 0]]
        self.assertEqual(expected,result)

    def test_ascending_pairs_2(self):
        input = [[-4, -3], [3,-6],[5]]
        result = hw1.ascending_pairs(input)
        expected = [[-4, -3], [-6, 3],[5]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        input1 = Price(59, 99)
        input2 = Price(0, 1)
        result = hw1.add_prices(input1, input2)
        expected = Price(60, 0)
        self.assertEqual(result, expected)

    def test_add_prices_2(self):
        input1 = Price(5, 63)
        input2 = Price(7, 42)
        result = hw1.add_prices(input1, input2)
        expected = Price(13, 5)
        self.assertEqual(result, expected)

    # Part 5
    def test_rectangle_area_1(self):
        input = Rectangle(Point(3,7), Point(4, 4))
        result = hw1.rectangle_area(input)
        expected = 3
        self.assertEqual(result, expected)

    def test_rectangle_area_2(self):
        input = Rectangle(Point(0,0), Point(5, -4))
        result = hw1.rectangle_area(input)
        expected = 20
        self.assertEqual(result, expected)


    # Part 6

    def test_books_by_author_1(self):
        input1 = "Brandon Sanderson"
        book1 = Book(["Brandon Sanderson"], "The Way of Kings")
        book2 = Book(["Brandon Sanderson"], "Skyward")
        book3 = Book(["Kami Garcia", "Margaret Stohl"], "Beautiful Creatures")
        input2 = [book1, book2, book3]
        result = hw1.books_by_author(input1, input2)
        expected = [book1, book2]
        self.assertEqual(result, expected)

    def test_books_by_author_2(self):
        input1 = "Stephen King"
        book1 = Book(["Stephen King"], "The Shining")
        book2 = Book(["J. K. Rowling"], "Harry Potter")
        book3 = Book(["George Orwell", "Margaret Stohl"], "1984")
        input2 = [book1, book2, book3]
        result = hw1.books_by_author(input1, input2)
        expected = [book1]
        self.assertEqual(result, expected)

    # Part 7
    def test_circle_bound_1(self):
        input = Rectangle(Point(0, 4), Point(3, 0))
        result = hw1.circle_bound(input)
        expected = Circle(Point(1.5, 2), 2.5)
        self.assertEqual(result,expected)

    def test_circle_bound_2(self):
        input = Rectangle(Point(-10, 7), Point(5, 3))
        result = hw1.circle_bound(input)
        expected = Circle(Point(-2.5, 5.0), pow(241, 0.5) * 0.5)
        self.assertEqual(result,expected)

    # Part 8
    def test_below_pay_average_1(self):
        input = [Employee("Kazuki", 5),
                 Employee("Orestis", 2),
                 Employee("Lucia", 9)]
        result = hw1.below_pay_average(input)
        expected = ["Kazuki", "Orestis"]
        self.assertEqual(result, expected)

    def test_below_pay_average_2(self):
        input = [Employee("Danielle", 7),
                 Employee("Leo", 8),
                 Employee("Maria", 8),
                 Employee("Anna",10),
                 Employee("Benjamin", 6),
                 Employee("Jade", 1)]

        result = hw1.below_pay_average(input)
        expected = ["Benjamin", "Jade"]
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
