import unittest

class TestPaginationLinks(unittest.TestCase):
    def test_first_link(self):
        self.assertEqual(PaginationLinks("http://example.com", 5, 1)["first"], "http://example.com?page=1")

    def test_last_link(self):
        self.assertEqual(PaginationLinks("http://example.com", 5, 1)["last"], "http://example.com?page=5")

    def test_prev_link(self):
        self.assertEqual(PaginationLinks("http://example.com", 5, 2)["prev"], "http://example.com?page=1")

    def test_next_link(self):
        self.assertEqual(PaginationLinks("http://example.com", 5, 4)["next"], "http://example.com?page=5")

    def test_prev_link_on_first_page(self):
        self.assertNotIn("prev", PaginationLinks("http://example.com", 5, 1)["links"])

    def test_next_link_on_last_page(self):
        self.assertNotIn("next", PaginationLinks("http://example.com", 5, 5)["links"])

    def test_base_url_with_query_string(self):
        self.assertEqual(PaginationLinks("http://example.com?foo=bar", 5, 1)["first"], "http://example.com?foo=bar&page=1")

    def test_invalid_current_page(self):
        self.assertEqual(PaginationLinks("http://example.com", 5, 10)["current_page"], 5)

if __name__ == '__main__':
    unittest.main()
