import unittest

class TestPaginator(unittest.TestCase):
    def setUp(self):
        self.test_data = [f"item_{i}" for i in range(1, 101)]
        self.paginator = Paginator(self.test_data, page_size=10)

    def test_total_pages_calculation(self):
        self.assertEqual(self.paginator.total_pages, 10)

    def test_get_page_valid(self):
        page_data = self.paginator.get_page(1)
        self.assertEqual(len(page_data), 10)
        self.assertEqual(page_data[0], "item_1")
        self.assertEqual(page_data[9], "item_10")

    def test_get_page_invalid(self):
        self.assertEqual(self.paginator.get_page(0), [])
        self.assertEqual(self.paginator.get_page(11), [])

    def test_get_page_info(self):
        page_info = self.paginator.get_page_info(1)
        self.assertEqual(page_info["current_page"], 1)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], True)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 10)

    def test_get_page_info_last_page(self):
        page_info = self.paginator.get_page_info(10)
        self.assertEqual(page_info["current_page"], 10)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], True)
        self.assertEqual(len(page_info["data"]), 10)

    def test_get_page_info_middle_page(self):
        page_info = self.paginator.get_page_info(5)
        self.assertEqual(page_info["current_page"], 5)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], True)
        self.assertEqual(page_info["has_prev"], True)
        self.assertEqual(len(page_info["data"]), 10)

    def test_get_page_info_zero_page(self):
        page_info = self.paginator.get_page_info(0)
        self.assertEqual(page_info["current_page"], 0)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_negative_page(self):
        page_info = self.paginator.get_page_info(-1)
        self.assertEqual(page_info["current_page"], -1)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)

    def test_get_page_info_large_page(self):
        page_info = self.paginator.get_page_info(100)
        self.assertEqual(page_info["current_page"], 100)
        self.assertEqual(page_info["total_pages"], 10)
        self.assertEqual(page_info["has_next"], False)
        self.assertEqual(page_info["has_prev"], False)
        self.assertEqual(len(page_info["data"]), 0)