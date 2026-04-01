import unittest

class TestSimpleTemplate(unittest.TestCase):
    def test_render_basic(self):
        template = SimpleTemplate("Hello {{name}}!")
        context = {"name": "Alice"}
        self.assertEqual(template.render(context), "Hello Alice!")

    def test_render_multiple(self):
        template = SimpleTemplate("Hello {{name}}, you are {{age}} years old.")
        context = {"name": "Bob", "age": 25}
        self.assertEqual(template.render(context), "Hello Bob, you are 25 years old.")

    def test_render_missing_key(self):
        template = SimpleTemplate("Hello {{name}}!")
        context = {"name": "Charlie"}
        self.assertEqual(template.render(context), "Hello Charlie!")

    def test_render_empty_context(self):
        template = SimpleTemplate("Hello {{name}}!")
        context = {}
        self.assertEqual(template.render(context), "Hello !")

    def test_render_special_chars(self):
        template = SimpleTemplate("Hello {{name}}! {{special}}")
        context = {"name": "Alice", "special": "!"}
        self.assertEqual(template.render(context), "Hello Alice! !")

    def test_render_complex_template(self):
        template = SimpleTemplate("Welcome to {{location}}! Your {{role}} is {{title}}.")
        context = {"location": "Paris", "role": "Developer", "title": "Senior"}
        self.assertEqual(template.render(context), "Welcome to Paris! Your Developer is Senior.")

    def test_render_with_spaces(self):
        template = SimpleTemplate("Hello {{name}}! How are you?")
        context = {"name": "David"}
        self.assertEqual(template.render(context), "Hello David! How are you?")

    def test_render_with_numbers(self):
        template = SimpleTemplate("Your score is {{score}}.")
        context = {"score": 95}
        self.assertEqual(template.render(context), "Your score is 95.")

    def test_render_with_unicode(self):
        template = SimpleTemplate("Hello {{name}}! 你好")
        context = {"name": "张三"}
        self.assertEqual(template.render(context), "Hello 张三! 你好")

    def test_render_with_list(self):
        template = SimpleTemplate("Your items are {{items}}.")
        context = {"items": ["apple", "banana"]}
        self.assertEqual(template.render(context), "Your items are ['apple', 'banana'].")

    def test_render_with_none(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": None}
        self.assertEqual(template.render(context), "Your value is None.")

    def test_render_with_boolean(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": True}
        self.assertEqual(template.render(context), "Your value is True.")

    def test_render_with_float(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": 3.14}
        self.assertEqual(template.render(context), "Your value is 3.14.")

    def test_render_with_string(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": "string"}
        self.assertEqual(template.render(context), "Your value is string.")

    def test_render_with_integer(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": 42}
        self.assertEqual(template.render(context), "Your value is 42.")

    def test_render_with_empty_string(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": ""}
        self.assertEqual(template.render(context), "Your value is .")

    def test_render_with_special_characters_in_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": "value with !@#$%^&*()"}
        self.assertEqual(template.render(context), "Your value is value with !@#$%^&*().")

    def test_render_with_special_characters_in_template(self):
        template = SimpleTemplate("Your value is {{value}}! {{special}}")
        context = {"value": "value", "special": "!@#$%^&*()"}
        self.assertEqual(template.render(context), "Your value is value! !@#$%^&*().")

    def test_render_with_multiple_occurrences(self):
        template = SimpleTemplate("Hello {{name}}! Hello {{name}}!")
        context = {"name": "Alice"}
        self.assertEqual(template.render(context), "Hello Alice! Hello Alice!")

    def test_render_with_nested_templates(self):
        template = SimpleTemplate("Hello {{name}}! {{greeting}}")
        context = {"name": "Alice", "greeting": "Hello"}
        self.assertEqual(template.render(context), "Hello Alice! Hello")

    def test_render_with_empty_string_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": ""}
        self.assertEqual(template.render(context), "Your value is .")

    def test_render_with_none_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": None}
        self.assertEqual(template.render(context), "Your value is None.")

    def test_render_with_boolean_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": True}
        self.assertEqual(template.render(context), "Your value is True.")

    def test_render_with_float_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": 3.14}
        self.assertEqual(template.render(context), "Your value is 3.14.")

    def test_render_with_string_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": "string"}
        self.assertEqual(template.render(context), "Your value is string.")

    def test_render_with_integer_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": 42}
        self.assertEqual(template.render(context), "Your value is 42.")

    def test_render_with_empty_string_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": ""}
        self.assertEqual(template.render(context), "Your value is .")

    def test_render_with_special_characters_in_value(self):
        template = SimpleTemplate("Your value is {{value}}.")
        context = {"value": "value with !@#$%^&*()"}
        self.assertEqual(template.render(context), "Your value is value with !@#$%^&*().")

    def test_render_with_special_characters_in_template(self):
        template = SimpleTemplate("Your value is {{value}}! {{special}}")
        context = {"value": "value", "special": "!@#$%^&*()"}
        self.assertEqual(template.render(context