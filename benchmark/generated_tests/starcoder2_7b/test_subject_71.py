import unittest

class TestGenerateBookReviewHtml(unittest.TestCase):
    def test_generate_book_review_html(self):
        self.assertEqual(generate_book_review_html("The Hobbit", "", "A hobbit is a small person with a long nose.", "adventure, fantasy, magic"), "<h1>The Hobbit</h1>\n<h2>By </h2>\n<p>A hobbit is a small person with a long nose.</p>\n<h3>Themes:</h3>\n<ul>\n<li>adventure</li>\n<li>fantasy</li>\n<li>magic</li>\n</ul>")

if __name__ == '__main__':
    unittest.main()