import unittest

class TestPubSubBus(unittest.TestCase):
    def setUp(self):
        self.bus = PubSubBus()
        self.handlers = []

    def test_subscribe_exact_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_wildcard(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_multiple_topics(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.subscribe("user.updated", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)
        self.bus.publish("user.updated", {"id": 2})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_multiple_wildcards(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.subscribe("user.*.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 2)

    def test_publish_nonexistent_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("nonexistent", {"id": 1})
        self.assertEqual(len(self.handlers), 0)

    def test_publish_with_payload(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1, "name": "John"})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_same_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_different_topics(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.subscribe("user.updated", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)
        self.bus.publish("user.updated", {"id": 2})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_and_publish_wildcard(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_multiple_wildcards(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.subscribe("user.*.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_and_publish_nonexistent_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("nonexistent", {"id": 1})
        self.assertEqual(len(self.handlers), 0)

    def test_subscribe_and_publish_with_payload(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1, "name": "John"})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_same_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_different_topics(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.subscribe("user.updated", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)
        self.bus.publish("user.updated", {"id": 2})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_and_publish_wildcard(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_multiple_wildcards(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.subscribe("user.*.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_and_publish_nonexistent_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("nonexistent", {"id": 1})
        self.assertEqual(len(self.handlers), 0)

    def test_subscribe_and_publish_with_payload(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1, "name": "John"})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_same_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_different_topics(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.subscribe("user.updated", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)
        self.bus.publish("user.updated", {"id": 2})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_and_publish_wildcard(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_multiple_wildcards(self):
        self.bus.subscribe("user.*", self.handlers.append)
        self.bus.subscribe("user.*.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 2)

    def test_subscribe_and_publish_nonexistent_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("nonexistent", {"id": 1})
        self.assertEqual(len(self.handlers), 0)

    def test_subscribe_and_publish_with_payload(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1, "name": "John"})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_same_topic(self):
        self.bus.subscribe("user.created", self.handlers.append)
        self.bus.publish("user.created", {"id": 1})
        self.assertEqual(len(self.handlers), 1)

    def test_subscribe_and_publish_different_topics(self):