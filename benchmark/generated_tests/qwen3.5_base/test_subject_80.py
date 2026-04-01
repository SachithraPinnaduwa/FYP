import unittest

class TestAStarPathFinder(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.start = (0, 0)
        self.goal = (4, 4)

    def test_find_path(self):
        path_finder = AStarPathFinder(self.grid)
        path = path_finder.find_path(self.start, self.goal)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])

    def test_find_path_with_obstacles(self):
        grid_with_obstacles = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        path_finder = AStarPathFinder(grid_with_obstacles)
        path = path_finder.find_path(self.start, self.goal)
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])

    def test_find_path_with_no_path(self):
        grid_no_path = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        path_finder = AStarPathFinder(grid_no_path)
        path = path_finder.find_path((0, 0), (4, 4))
        self.assertEqual(path, [])

    def test_find_path_with_start_or_goal_as_obstacle(self):
        grid_start_obstacle = [
            [1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        path_finder = AStarPathFinder(grid_start_obstacle)
        path = path_finder.find_path((0, 0), (4, 4))
        self.assertEqual(path, [])

    def test_find_path_with_goal_as_obstacle(self):
        grid_goal_obstacle = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]
        path_finder = AStarPathFinder(grid_goal_obstacle)
        path = path_finder.find_path((0, 0), (4, 4))
        self.assertEqual(path, [])

    def test_find_path_with_empty_grid(self):
        empty_grid = []
        path_finder = AStarPathFinder(empty_grid)
        path = path_finder.find_path((0, 0), (0, 0))
        self.assertEqual(path, [])

    def test_find_path_with_single_cell_grid(self):
        single_cell_grid = [[0]]
        path_finder = AStarPathFinder(single_cell_grid)
        path = path_finder.find_path((0, 0), (0, 0))
        self.assertEqual(path, [(0, 0)])

    def test_find_path_with_single_cell_grid_obstacle(self):
        single_cell_grid_obstacle = [[1]]
        path_finder = AStarPathFinder(single_cell_grid_obstacle)
        path = path_finder.find_path((0, 0), (0, 0))
        self.assertEqual(path, [])

    def test_find_path_with_large_grid(self):
        large_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        path_finder = AStarPathFinder(large_grid)
        path = path_finder.find_path((0, 0), (9, 9))
        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9,