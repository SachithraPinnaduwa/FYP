def generate_book_review_html(title, author, plot, themes):
    themes_list = themes.split(",")
    themes_html = ""
    for theme in themes_list:
        themes_html += "<li>" + theme.strip() + "</li>"
    html = "<h1>" + title + "</h1>\n<h2>By " + author + "</h2>\n<p>" + plot + "</p>\n<h3>Themes:</h3>\n<ul>\n" + themes_html + "</ul>"
    return html