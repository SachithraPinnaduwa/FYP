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
    def test_generate_book_review_html(self):
        self.assertEqual(generate_book_review_html("To Kill a Mockingbird", "Harper Lee", "The trial of Tom Robinson, an African American man falsely accused of raping a white woman, in the fictional town of Maycomb, Alabama, during the Great Depression.", "racism, injustice, childhood, loss"), '<h1>To Kill a Mockingbird</h1>\n<h2>By Harper Lee</h2>\n<p>The trial of Tom Robinson, an African American man falsely accused of raping a white woman, in the fictional town of Maycomb, Alabama, during the Great Depression.</p>\n<h3>Themes:</h3>\n<ul>\n<li>racism</li>\n<li>injustice</li>\n<li>childhood</li>\n<li>loss</li>\n</ul>')
        self.assertEqual(generate_book_review_html("1984", "George Orwell", "The story of Winston Smith, a man living in the dystopian world of Oceania, where the government controls every aspect of people's lives.", "totalitarianism, surveillance, love, rebellion"), '<h1>1984</h1>\n<h2>By George Orwell</h2>\n<p>The story of Winston Smith, a man living in the dystopian world of Oceania, where the government controls every aspect of people\'s lives.</p>\n<h3>Themes:</h3>\n<ul>\n<li>totalitarianism</li>\n<li>surveillance</li>\n<li>love</li>\n<li>rebellion</li>\n</ul>')
        self.assertEqual(generate_book_review_html("Pride and Prejudice", "Jane Austen", "The story of Elizabeth Bennet, a young woman from a wealthy family, and her relationships with the men in her life.", "marriage, love, class, manners, society"), '<h1>Pride and Prejudice</h1>\n<h2>By Jane Austen</h2>\n<p>The story of Elizabeth Bennet, a young woman from a wealthy family, and her relationships with the men in her life.</p>\n<h3>Themes:</h3>\n<ul>\n<li>marriage</li>\n<li>love</li>\n<li>class</li>\n<li>manners</li>\n<li>society</li>\n</ul>')
        self.assertEqual(generate_book_review_html("The Great Gatsby", "F. Scott Fitzgerald", "The story of Jay Gatsby, a millionaire who throws extravagant parties in hopes of winning back his lost love, Daisy Buchanan.", "wealth, love, past, dreams, reality"), '<h1>The Great Gatsby</h1>\n<h2>By F. Scott Fitzgerald</h2>\n<p>The story of Jay Gatsby, a millionaire who throws extravagant parties in hopes of winning back his lost love, Daisy Buchanan.</p>\n<h3>Themes:</h3>\n<ul>\n<li>wealth</li>\n<li>love</li>\n<li>past</li>\n<li>dreams</li>\n<li>reality</li>\n</ul>')
        self.assertEqual(generate_book_review_html("Moby Dick", "Herman Melville", "The story of Ishmael, a sailor who joins a whaling ship and becomes obsessed with hunting the white whale, Moby Dick.", "whaling, obsession, nature, man vs. nature, fate"), '<h1>Moby Dick</h1>\n<h2>By Herman Melville</h2>\n<p>The story of Ishmael, a sailor who joins a whaling ship and becomes obsessed with hunting the white whale, Moby Dick.</p>\n<h3>Themes:</h3>\n<ul>\n<li>whaling</li>\n<li>obsession</li>\n<li>nature</li>\n<li>man vs. nature</li>\n<li>fate</li>\n</ul>')

if __name__ == '__main__':
    unittest.main()