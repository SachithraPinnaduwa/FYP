from subject_71 import *

import unittest

def generate_book_review_html(title, author, plot, themes):
    themes_list = themes.split(",")
    themes_html = ""
    for theme in themes_list:
        themes_html += "<li>" + theme.strip() + "</li>"
    html = "<h1>" + title + "</h1>\n<h2>By " + author + "</h2>\n<p>" + plot + "</p>\n<h3>Themes:</h3>\n<ul>\n" + themes_html + "</ul>"
    return html

class TestGenerateBookReviewHTML(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(generate_book_review_html('The Great Gatsby', 'F. Scott Fitzgerald', 'The story of Jay Gatsby and his love for Daisy Buchanan.', 'love, wealth, class'), '<h1>The Great Gatsby</h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>The story of Jay Gatsby and his love for Daisy Buchanan.</p>\n<h3>Themes:</h3>\n<ul>\n<li>love</li>\n<li>wealth</li>\n<li>class</li>\n</ul>')

    def test_edge_case_empty_title(self):
        self.assertEqual(generate_book_review_html('', 'F. Scott Fitzgerald', 'The story of Jay Gatsby and his love for Daisy Buchanan.', 'love, wealth, class'), '<h1></h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>The story of Jay Gatsby and his love for Daisy Buchanan.</p>\n<h3>Themes:</h3>\n<ul>\n<li>love</li>\n<li>wealth</li>\n<li>class</li>\n</ul>')

    def test_edge_case_none_author(self):
        self.assertEqual(generate_book_review_html('The Great Gatsby', None, 'The story of Jay Gatsby and his love for Daisy Buchanan.', 'love, wealth, class'), '<h1>The Great Gatsby</h1>\n<h2>By None</h2>\n<p>The story of Jay Gatsby and his love for Daisy Buchanan.</p>\n<h3>Themes:</h3>\n<ul>\n<li>love</li>\n<li>wealth</li>\n<li>class</li>\n</ul>')

    def test_error_handling_non_string_plot(self):
        with self.assertRaises(TypeError):
            generate_book_review_html('The Great Gatsby', 'F. Scott Fitzgerald', 123, 'love, wealth, class')

if __name__ == '__main__':
    unittest.main()