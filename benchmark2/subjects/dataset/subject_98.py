import math

def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    elif b**2 + c**2 == a**2:
        return True
    elif a**2 + c**2 == b**2:
        return True
    else:
        return False

def is_equilateral_triangle(a, b, c):
    if a == b and b == c:
        return True
    else:
        return False

def is_isosceles_triangle(a, b, c):
    if a == b or b == c or a == c:
        return True
    else:
        return False

def calculate_area(a):
    area = (math.sqrt(3) / 4) * a**2
    return area

def calculate_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def calculate_angles(a, b, c):
    angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = 180 - angle_a - angle_b
    return angle_a, angle_b, angle_c