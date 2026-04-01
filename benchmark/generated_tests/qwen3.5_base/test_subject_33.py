import unittest

class TestXMLBuilder(unittest.TestCase):
    def test_empty_root(self):
        builder = XMLBuilder("root")
        self.assertEqual(builder.render(), "<root />\n")

    def test_single_child(self):
        builder = XMLBuilder("root")
        child = builder.add_child("child")
        child.set_text("text")
        self.assertEqual(builder.render(), "<root>\n  text\n</root>\n")

    def test_nested_children(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child2 = builder.add_child("child2")
        child1.set_text("text1")
        child2.set_text("text2")
        self.assertEqual(builder.render(), "<root>\n  child1\n    text1\n  child2\n    text2\n</root>\n")

    def test_attributes(self):
        builder = XMLBuilder("root")
        builder.add_attribute("key", "value")
        self.assertEqual(builder.render(), "<root key=\"value\" />\n")

    def test_attributes_and_text(self):
        builder = XMLBuilder("root")
        builder.add_attribute("key", "value")
        builder.set_text("text")
        self.assertEqual(builder.render(), "<root key=\"value\">\n  text\n</root>\n")

    def test_attributes_and_children(self):
        builder = XMLBuilder("root")
        builder.add_attribute("key", "value")
        child = builder.add_child("child")
        child.set_text("text")
        self.assertEqual(builder.render(), "<root key=\"value\">\n  child\n    text\n</root>\n")

    def test_multiple_attributes(self):
        builder = XMLBuilder("root")
        builder.add_attribute("key1", "value1")
        builder.add_attribute("key2", "value2")
        self.assertEqual(builder.render(), "<root key1=\"value1\" key2=\"value2\" />\n")

    def test_multiple_attributes_and_text(self):
        builder = XMLBuilder("root")
        builder.add_attribute("key1", "value1")
        builder.add_attribute("key2", "value2")
        builder.set_text("text")
        self.assertEqual(builder.render(), "<root key1=\"value1\" key2=\"value2\">\n  text\n</root>\n")

    def test_multiple_attributes_and_children(self):
        builder = XMLBuilder("root")
        builder.add_attribute("key1", "value1")
        builder.add_attribute("key2", "value2")
        child = builder.add_child("child")
        child.set_text("text")
        self.assertEqual(builder.render(), "<root key1=\"value1\" key2=\"value2\">\n  child\n    text\n</root>\n")

    def test_deeply_nested_children(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child2 = child1.add_child("child2")
        child3 = child2.add_child("child3")
        child3.set_text("text")
        self.assertEqual(builder.render(), "<root>\n  child1\n    child2\n      child3\n        text\n</root>\n")

    def test_deeply_nested_children_with_attributes(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child1.add_attribute("key", "value")
        child2 = child1.add_child("child2")
        child3 = child2.add_child("child3")
        child3.set_text("text")
        self.assertEqual(builder.render(), "<root>\n  child1 key=\"value\"\n    child2\n      child3\n        text\n</root>\n")

    def test_deeply_nested_children_with_attributes_and_text(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child1.add_attribute("key", "value")
        child2 = child1.add_child("child2")
        child3 = child2.add_child("child3")
        child3.set_text("text")
        child1.set_text("text1")
        self.assertEqual(builder.render(), "<root>\n  child1 key=\"value\"\n    text1\n    child2\n      child3\n        text\n</root>\n")

    def test_multiple_children_with_attributes(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child1.add_attribute("key", "value")
        child2 = builder.add_child("child2")
        child2.add_attribute("key", "value")
        child1.set_text("text1")
        child2.set_text("text2")
        self.assertEqual(builder.render(), "<root>\n  child1 key=\"value\"\n    text1\n  child2 key=\"value\"\n    text2\n</root>\n")

    def test_multiple_children_with_attributes_and_text(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child1.add_attribute("key", "value")
        child2 = builder.add_child("child2")
        child2.add_attribute("key", "value")
        child1.set_text("text1")
        child2.set_text("text2")
        child1.add_attribute("key2", "value2")
        self.assertEqual(builder.render(), "<root>\n  child1 key=\"value\" key2=\"value2\"\n    text1\n  child2 key=\"value\"\n    text2\n</root>\n")

    def test_multiple_children_with_attributes_and_text_and_deeply_nested(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child1.add_attribute("key", "value")
        child2 = builder.add_child("child2")
        child2.add_attribute("key", "value")
        child1.set_text("text1")
        child2.set_text("text2")
        child1.add_attribute("key2", "value2")
        child3 = child1.add_child("child3")
        child3.set_text("text3")
        self.assertEqual(builder.render(), "<root>\n  child1 key=\"value\" key2=\"value2\"\n    text1\n    child3\n      text3\n  child2 key=\"value\"\n    text2\n</root>\n")

    def test_multiple_children_with_attributes_and_text_and_deeply_nested_with_attributes(self):
        builder = XMLBuilder("root")
        child1 = builder.add_child("child1")
        child1.add_attribute("key", "value")
        child2 = builder.add_child("child2")
        child2.add_attribute("key", "value")
        child1.set_text("text1")
        child2.set_text("text2")
        child1.add_attribute("key2", "value2")
        child3 = child1.add_child("child3")
        child3.add_attribute("key