import math

def test_is_right_triangle():
    # Test case for a right-angled triangle
    assert is_right_triangle(3, 4, 5) == True
    # Test case for an isosceles triangle (not right-angled)
    assert is_right_triangle(5, 5, 8) == False
    # Test case for an equilateral triangle (not right-angled)
    assert is_right_triangle(6, 6, 6) == False

def test_is_equilateral_triangle():
    # Test case for an equilateral triangle
    assert is_equilateral_triangle(5, 5, 5) == True
    # Test case for a right-angled triangle (not equilateral)
    assert is_equilateral_triangle(3, 4, 5) == False
    # Test case for an isosceles triangle (not equilateral)
    assert is_equilateral_triangle(5, 5, 8) == False

def test_is_isosceles_triangle():
    # Test case for an isosceles triangle
    assert is_isosceles_triangle(5, 5, 8) == True
    # Test case for a right-angled triangle (not isosceles)
    assert is_isosceles_triangle(3, 4, 5) == False
    # Test case for an equilateral triangle (not isosceles)
    assert is_isosceles_triangle(6, 6, 6) == False

def test_calculate_area():
    # Test case for an equilateral triangle
    assert math.isclose(calculate_area(6), 15.588457268119896, rel_tol=1e-9) == True
    # Test case for a right-angled triangle
    assert math.isclose(calculate_area(3), 3.897114317029974, rel_tol=1e-9) == True
    # Test case for an isosceles triangle
    assert math.isclose(calculate_area(5), 10.825317547305485, rel_tol=1e-9) == True

def test_calculate_perimeter():
    # Test case for an equilateral triangle
    assert calculate_perimeter(6, 6, 6) == 18
    # Test case for a right-angled triangle
    assert calculate_perimeter(3, 4, 5) == 12
    # Test case for an isosceles triangle
    assert calculate_perimeter(5, 5, 8) == 18

def test_calculate_angles():
    # Test case for an equilateral triangle
    assert calculate_angles(6, 6, 6) == (60.0, 60.0, 60.0)
    # Test case for a right-angled triangle
    assert calculate_angles(3, 4, 5) == (36.86989764584402, 53.13010235415598, 90.0)
    # Test case for an isosceles triangle
    assert calculate_angles(5, 5, 8) == (53.13010235415598, 53.13010235415598, 73.73979529168804)