import unittest

def generate_book_review_html(title, author, plot, themes):
    themes_list = themes.split(",")
    themes_html = ""
    for theme in themes_list:
        themes_html += "<li>" + theme.strip() + "</li>"
    html = "<h1>" + title + "</h1>\n<h2>By " + author + "</h2>\n<p>" + plot + "</p>\n<h3>Themes:</h3>\n<ul>\n" + themes_html + "</ul>"
    return html

class TestGenerateBookReviewHTML(unittest.TestCase):

    def test_generate_book_review_html(self):
        # Test with all parameters provided
        result = generate_book_review_html("To Kill a Mockingbird", "Harper Lee", "A story of racial injustice in the American South.", "Racial injustice, Coming of age, Atticus Finch")
        expected = """<h1>To Kill a Mockingbird</h1>
<h2>By Harper Lee</h2>
<p>A story of racial injustice in the American South.</p>
<h3>Themes:</h3>
<ul>
<li>Racial injustice</li>
<li>Coming of age</li>
<li>Atticus Finch</li>
</ul>"""
        self.assertEqual(result, expected)

    def test_empty_themes(self):
        # Test with empty themes parameter
        result = generate_book_review_html("The Great Gatsby", "F. Scott Fitzgerald", "The story of Jay Gatsby and his love for Daisy Buchanan.", "")
        expected = """<h1>The Great Gatsby</h1>
<h2>By F. Scott Fitzgerald</h2>
<p>The story of Jay Gatsby and his love for Daisy Buchanan.</p>
<h3>Themes:</h3>
<ul>
</ul>"""
        self.assertEqual(result, expected)

    def test_single_theme(self):
        # Test with single theme
        result = generate_book_review_html("Pride and Prejudice", "Jane Austen", "The story of Elizabeth Bennet and her relationships with Mr. Darcy and others.", "Love, Marriage, Social class")
        expected = """<h1>Pride and Prejudice</h1>
<h2>By Jane Austen</h2>
<p>The story of Elizabeth Bennet and her relationships with Mr. Darcy and others.</p>
<h3>Themes:</h3>
<ul>
<li>Love</li>
<li>Marriage</li>
<li>Social class</li>
</ul>"""
        self.assertEqual(result, expected)

    def test_no_spaces_in_themes(self):
        # Test with no spaces between themes
        result = generate_book_review_html("Moby Dick", "Herman Melville", "The story of the white whale Moby Dick.", "Whaling, Revenge, Fate")
        expected = """<h1>Moby Dick</h1>
<h2>By Herman Melville</h2>
<p>The story of the white whale Moby Dick.</p>
<h3>Themes:</h3>
<ul>
<li>Whaling</li>
<li>Revenge</li>
<li>Fate</li>
</ul>"""
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()