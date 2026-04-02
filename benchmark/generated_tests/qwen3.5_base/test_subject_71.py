import unittest

class TestGenerateBookReviewHTML(unittest.TestCase):
    def test_generate_book_review_html(self):
        title = "The Great Gatsby"
        author = "F. Scott Fitzgerald"
        plot = "A story of love and loss in the Jazz Age."
        themes = "wealth, love, ambition"
        expected = "<h1>The Great Gatsby</h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>A story of love and loss in the Jazz Age.</p>\n<h3>Themes:</h3>\n<ul>\n<li>wealth</li>\n<li>love</li>\n<li>ambition</li>\n</ul>"
        result = generate_book_review_html(title, author, plot, themes)
        self.assertEqual(result, expected)

    def test_generate_book_review_html_with_empty_themes(self):
        title = "The Great Gatsby"
        author = "F. Scott Fitzgerald"
        plot = "A story of love and loss in the Jazz Age."
        themes = ""
        expected = "<h1>The Great Gatsby</h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>A story of love and loss in the Jazz Age.</p>\n<h3>Themes:</h3>\n<ul>\n</ul>"
        result = generate_book_review_html(title, author, plot, themes)
        self.assertEqual(result, expected)

    def test_generate_book_review_html_with_single_theme(self):
        title = "The Great Gatsby"
        author = "F. Scott Fitzgerald"
        plot = "A story of love and loss in the Jazz Age."
        themes = "wealth"
        expected = "<h1>The Great Gatsby</h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>A story of love and loss in the Jazz Age.</p>\n<h3>Themes:</h3>\n<ul>\n<li>wealth</li>\n</ul>"
        result = generate_book_review_html(title, author, plot, themes)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
