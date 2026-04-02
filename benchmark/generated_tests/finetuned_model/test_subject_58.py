from math import pi, radians, sin, cos, acos

def calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec):
    # Convert degrees to radians
    observer_lat_rad = radians(observer_lat)
    celestial_dec_rad = radians(celestial_dec)
    celestial_ra_rad = radians(celestial_ra)
    observer_lon_rad = radians(observer_lon)

    # Calculate the topocentric distance using the provided formula
    phi = observer_lat_rad
    delta = celestial_dec_rad
    H = observer_lon_rad - celestial_ra_rad
    cos_d = sin(delta) * sin(phi) + cos(delta) * cos(phi) * cos(H)
    R = 149.6 * 10**6  # Mean distance of the celestial object from the Earth in km
    R_E = 6371  # Earth's mean radius in km
    topocentric_distance = R * acos(cos_d) / R_E

    return topocentric_distance

# Test cases
def test_calculate_topocentric_distance():
    # Test case 1: Observer at the equator, celestial body directly above
    assert round(calculate_topocentric_distance(0, 0, 0, 90), 2) == 149.6, "Test case 1 failed"

    # Test case 2: Observer at the equator, celestial body directly below
    assert round(calculate_topocentric_distance(0, 0, 0, -90), 2) == 149.6, "Test case 2 failed"

    # Test case 3: Observer at the equator, celestial body at a 45-degree angle
    assert round(calculate_topocentric_distance(0, 0, 45, 0), 2) == 105.43, "Test case 3 failed"

    # Test case 4: Observer at the North Pole, celestial body directly above
    assert round(calculate_topocentric_distance(90, 0, 0, 90), 2) == 149.6, "Test case 4 failed"

    # Test case 5: Observer at the North Pole, celestial body directly below
    assert round(calculate_topocentric_distance(90, 0, 0, -90), 2) == 149.6, "Test case 5 failed"

    # Test case 6: Observer at the North Pole, celestial body at a 45-degree angle
    assert round(calculate_topocentric_distance(90, 0, 45, 0), 2) == 105.43, "Test case 6 failed"

    # Test case 7: Observer at the South Pole, celestial body directly above
    assert round(calculate_topocentric_distance(-90, 0, 0, 90), 2) == 149.6, "Test case 7 failed"

    # Test case 8: Observer at the South Pole, celestial body directly below
    assert round(calculate_topocentric_distance(-90, 0, 0, -90), 2) == 149.6, "Test case 8 failed"

    # Test case 9: Observer at the South Pole, celestial body at a 45-degree angle
    assert round(calculate_topocentric_distance(-90, 0, 45, 0), 2) == 105.43, "Test case 9 failed"

    # Test case 10: Observer at a random location, celestial body at a random angle
    assert round(calculate_topocentric_distance(30, 45, 60, 30), 2) == 126.55, "Test case 10 failed"

    print("All test cases passed!")

test_calculate_topocentric_distance()