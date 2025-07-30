# math_operations.py
import math

def circle_area(radius):
    return round(3.14159 * radius ** 2, 2)

def rectangle_area(width, height):
    return width * height

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
