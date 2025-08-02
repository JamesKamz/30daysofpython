#day 11 of 30 days with python challenge
from math import pi
def add_two_numbers(num1, num2):
    return num1 + num2

def area_of_circle(radius):
    area = pi * (radius ** 2)
    return area

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"Invalid input: {num} is not a number.")
    return total

def convert_celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def check_season(month):
    if month in ["September", "October", "November"]:
        season =  'Autumn'
    elif month in ["December", "January", "February"]:
        season =  'Winter'
    elif month in ["March", "April", "May"]:
        season =  'Spring'
    elif month in ["June", "July", "August"]:
        season =  'Summer'
    else:
        print("Invalid month entered.")
    return season

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined (division by zero). The line is vertical.")
    slope = (y2 - y1) / (x2 - x1)
    return slope

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return None
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return None
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return (root1, root2)

def print_list(lst):
    if not lst:
        print("The list is empty.")
    else:
        for item in lst:
            print(item)

def reverse_list(lst):              
    if not lst:
        print("The list is empty.")
    else:
        reversed_lst = lst[::-1]
        for item in reversed_lst:
            print(item)
            
def capitalize_list_items(lst):
    if not lst:
        print("The list is empty.")
    else:
        capitalized_lst = [item.capitalize() for item in lst]
        for item in capitalized_lst:
            print(item)     

def add_item_to_list(lst, item):
    if item in lst:
        print(f"{item} already exists in the list.")
    else:
        lst.append(item)
        print(f"{item} added to the list.")
    return lst

def remove_item_from_list(lst, item):
    if item in lst:
        lst.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")
    return lst  

def sum_of_numbers_in_list(lst):
    if not lst:
        print("The list is empty.")
        return 0
    total = sum(lst)
    print(f"The sum of the numbers in the list is: {total}")
    return total

def sum_of_odds(x):
    x=int(print("Enter a list of numbers separated by spaces: "))
    total = 0
    for num in x:
        if num % 2 != 0:
            total += num
    print(f"The sum of odd numbers in the list is: {total}")
    return total

def sum_of_even(x)
    x=int(print("Enter a list of numbers separated by spaces: "))
    total  =0
    for num in x:
        if num % 2 == 0:
            total += num
    print(f"The sum of even numbers in the list is: {total}")
    return total

#level 2