from idlelib.debugobj_r import remote_object_tree_item

import data

# Write your functions for each part in the space below.

# Part 1

# Count the vowels in a string
# Input: a string to count the vowels of
# Output: the integer count of vowels
def vowel_count(s : str) -> int:
    vowels = "aeiou"
    count = 0
    lower_s = s.lower()
    for c in lower_s:
        if c in vowels:
            count += 1

    return count


# Part 2

# Takes in a list of integer lists, and returns a new list that only has those lists which have a length of 2
# Input: A list of integer lists
# Output: A new list containing only the integer lists of length 2
def short_lists(lists : list[list[int]]) -> list[list[int]]:
    return_lists = []
    for num_list in lists:
        if len(num_list) == 2:
            return_lists.append(num_list.copy())
    return  return_lists

# Part 3

# Takes in a list lof integer lists, returning a new list where each integer list of length 2 is put in ascending order
# Input: A list of integer lists
# Output: A copy of the input, but where each integer list of length 2 is in ascending order
def ascending_pairs(lists: list[list[int]]) -> list[list[int]]:
    return_lists = []
    for num_list in lists:
        if len(num_list) == 2:
            new_list = [min(num_list[0], num_list[1]), max(num_list[0], num_list[1])]
            return_lists.append(new_list)
        else:
            return_lists.append(num_list.copy())


    return return_lists

# Part 4

from data import Price

# Add two prices
# Input: two price objects
# Output: a new price object with the sum of values
def add_prices(price1: Price, price2 : Price) -> Price:
    cents = price1.cents + price2.cents
    dollars = price1.dollars + price2.dollars
    dollars += cents // 100
    cents %= 100
    new_price = Price(dollars, cents)
    return  new_price

# Part 5

from data import Rectangle
from data import Point

# Calculate the area of a rectangle
# Input: A Rectangle object
# Output: The area as a float
def rectangle_area(rectangle: Rectangle) -> float:
    dimensions = width_and_height_of_rectangle(rectangle)
    return dimensions.x * dimensions.y

def width_and_height_of_rectangle(rectangle: Rectangle) -> Point:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.top_left.y - rectangle.bottom_right.y
    return Point(width, height)

# Part 6

from data import Book

# Gets the books in a list written by a given author
# Input: a string author name, and a list of books
# Output: List of books written by that author
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    return_books = []
    for book in books:
        if book.authors.__contains__(author_name):
            return_books.append(book)

    return return_books

# Part 7

from data import Circle

# Make a circle which circumscribes a given rectangle
# Input: a Rectangle
# Output: a Circle
def circle_bound(rectangle: Rectangle) -> Circle:
    return Circle(center_of_rectangle(rectangle), diagonal_length_of_rectangle(rectangle) * 0.5)

# Get the center point of a rectangle
# Input: a Rectangle
# Output: a Point
def center_of_rectangle(rectangle: Rectangle) -> Point:
    x = (rectangle.top_left.x + rectangle.bottom_right.x) * 0.5
    y = (rectangle.top_left.y + rectangle.bottom_right.y) * 0.5
    return Point(x,y)

# Gets the diagonal length of a rectangle (hypotenuse of height and width)
# Input: a Rectangle
# Output: a float length
def diagonal_length_of_rectangle(rectangle: Rectangle) -> float:
    dimensions = width_and_height_of_rectangle(rectangle)
    return pow(dimensions.x * dimensions.x + dimensions.y * dimensions.y, 0.5) # hypotenuse


# Part 8

from data import Employee

# Gets the names of employees that are paid below the average
# Input: list of employees
# Output: list of employee names
def below_pay_average(employees: list[Employee]) -> list[str]:
    if len(employees) == 0:
        return []

    employees_below_average = []

    average = average_pay(employees)
    for employee in employees:
        if employee.pay_rate < average:
            employees_below_average.append(employee.name)

    return employees_below_average

# Get the average pay
# Input: list of employees
# Output: average pay as float
def average_pay(employees: list[Employee]) -> int:
    total = 0
    for employee in employees:
        total += employee.pay_rate
    average = total / len(employees)
    return average


