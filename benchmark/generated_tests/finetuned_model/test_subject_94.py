def test_calculate_robot_locations():
    assert calculate_robot_locations(1) == 4
    assert calculate_robot_locations(2) == 4
    assert calculate_robot_locations(3) == 12
    assert calculate_robot_locations(4) == 16
    assert calculate_robot_locations(5) == 20
    assert calculate_robot_locations(6) == 32
    assert calculate_robot_locations(7) == 36
    assert calculate_robot_locations(8) == 48
    assert calculate_robot_locations(9) == 52
    assert calculate_robot_locations(10) == 64
    assert calculate_robot_locations(11) == 68
    assert calculate_robot_locations(12) == 80
    assert calculate_robot_locations(13) == 84
    assert calculate_robot_locations(14) == 96
    assert calculate_robot_locations(15) == 100
    assert calculate_robot_locations(1000) == 250500