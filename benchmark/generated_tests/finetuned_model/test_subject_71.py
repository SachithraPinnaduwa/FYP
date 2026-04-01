import unittest

class TestGenerateBookReviewHtml(unittest.TestCase):
    def test_generate_book_review_html(self):
        # Test case to check if the function generates HTML correctly
        title = "1984"
        author = "George Orwell"
        plot = "The story follows Winston Smith, a man who works as a low-ranking member of the Party's Thought Police."
        themes = "Dystopian society, Propaganda, Surveillance, Individualism, Totalitarianism"
        expected_output = '<h1>1984</h1>\n<h2>By George Orwell</h2>\n<p>The story follows Winston Smith, a man who works as a low-ranking member of the Party\'s Thought Police.</p>\n<h3>Themes:</h3>\n<ul>\n<li>Dystopian society</li>\n<li>Propaganda</li>\n<li>Surveillance</li>\n<li>Individualism</li>\n<li>Totalitarianism</li>\n</ul>'
        self.assertEqual(generate_book_review_html(title, author, plot, themes), expected_output)

    def test_generate_book_review_html_with_no_themes(self):
        # Test case to check if the function handles cases with no themes
        title = "To Kill a Mockingbird"
        author = "Harper Lee"
        plot = "The story is set in the fictional town of Maycomb, Alabama, in the 1930s."
        themes = ""
        expected_output = '<h1>To Kill a Mockingbird</h1>\n<h2>By Harper Lee</h2>\n<p>The story is set in the fictional town of Maycomb, Alabama, in the 1930s.</p>\n<h3>Themes:</h3>\n<ul>\n</ul>'
        self.assertEqual(generate_book_review_html(title, author, plot, themes), expected_output)

    def test_generate_book_review_html_with_one_theme(self):
        # Test case to check if the function handles cases with one theme
        title = "The Great Gatsby"
        author = "F. Scott Fitzgerald"
        plot = "The story follows Jay Gatsby, a wealthy man who throws extravagant parties in hopes of winning back his lost love."
        themes = "Opulence, Class, Identity"
        expected_output = '<h1>The Great Gatsby</h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>The story follows Jay Gatsby, a wealthy man who throws extravagant parties in hopes of winning back his lost love.</p>\n<h3>Themes:</h3>\n<ul>\n<li>Opulence</li>\n<li>Class</li>\n<li>Identity</li>\n</ul>'
        self.assertEqual(generate_book_review_html(title, author, plot, themes), expected_output)