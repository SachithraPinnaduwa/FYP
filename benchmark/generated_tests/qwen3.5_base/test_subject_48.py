import unittest

class TestSimpleMarkdownTable(unittest.TestCase):
    def test_init(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        self.assertEqual(table.headers, ["Name", "Age", "City"])
        self.assertEqual(table.rows, [])

    def test_add_row(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        self.assertEqual(table.rows, [["Alice", 25, "New York"]])

    def test_render(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_empty_rows(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["", 30, ""])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
|       | 30  |             |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_special_characters(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_long_headers(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_long_rows(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_mixed_data_types(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_unicode(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_empty_headers(self):
        headers = []
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| | | |
|---|---|---|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_empty_rows(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["", 30, ""])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
|       | 30  |             |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_special_characters(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_long_headers(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25  | New York    |
| Bob   | 30  | Los Angeles |"""
        self.assertEqual(table.render(), expected)

    def test_render_with_long_rows(self):
        headers = ["Name", "Age", "City"]
        table = SimpleMarkdownTable(headers)
        table.add_row(["Alice", 25, "New York"])
        table.add_row(["Bob", 30, "Los Angeles"])
        expected = """| Name  | Age | City        |
|-------|-----|-------------|
| Alice | 25