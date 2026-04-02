def test_max_marks_with_forgetfulness():
    # Test case 1
    chapters1 = [(1, 1), (2, 1)]
    total_time1 = 2
    assert max_marks_with_forgetfulness(chapters1, total_time1) == 2

    # Test case 2
    chapters2 = [(1, 1), (2, 2), (3, 3)]
    total_time2 = 3
    assert max_marks_with_forgetfulness(chapters2, total_time2) == 2

    # Test case 3
    chapters3 = [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
    total_time3 = 6
    assert max_marks_with_forgetfulness(chapters3, total_time3) == 9

    # Test case 4: Edge case with no time left
    chapters4 = [(1, 1)]
    total_time4 = 0
    assert max_marks_with_forgetfulness(chapters4, total_time4) == -float('inf')

    # Test case 5: Edge case with only one chapter
    chapters5 = [(5, 5)]
    total_time5 = 5
    assert max_marks_with_forgetfulness(chapters5, total_time5) == 5

    # Test case 6: Edge case with no chapters
    chapters6 = []
    total_time6 = 5
    assert max_marks_with_forgetfulness(chapters6, total_time6) == 0

    # Test case 7: Test with large number of chapters and time
    chapters7 = [(i, i) for i in range(1, 1001)]
    total_time7 = 1000
    assert max_marks_with_forgetfulness(chapters7, total_time7) == sum(i for i in range(2, 1001))

    # Test case 8: Test with negative marks and time
    chapters8 = [(-1, 1), (2, -2), (3, 3)]
    total_time8 = 3
    assert max_marks_with_forgetfulness(chapters8, total_time8) == 2

    # Test case 9: Test with large marks and time
    chapters9 = [(1000000000, 1), (2000000000, 2), (3000000000, 3)]
    total_time9 = 3
    assert max_marks_with_forgetfulness(chapters9, total_time9) == 2000000000

    # Test case 10: Test with zero marks and time
    chapters10 = [(0, 1), (0, 2), (0, 3)]
    total_time10 = 3
    assert max_marks_with_forgetfulness(chapters10, total_time10) == 0

    print("All test cases pass")