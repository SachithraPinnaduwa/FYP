import unittest

class TestDIContainer(unittest.TestCase):
    def setUp(self):
        self.container = DIContainer()

    def test_register_and_resolve(self):
        @staticmethod
        def factory():
            return "Service Instance"
        
        self.container.register("test_service", factory)
        result = self.container.resolve("test_service")
        self.assertEqual(result, "Service Instance")

    def test_singleton_behavior(self):
        @staticmethod
        def factory():
            return "Service Instance"
        
        self.container.register("singleton_service", factory, singleton=True)
        instance1 = self.container.resolve("singleton_service")
        instance2 = self.container.resolve("singleton_service")
        self.assertEqual(instance1, instance2)

    def test_non_singleton_behavior(self):
        @staticmethod
        def factory():
            return "Service Instance"
        
        self.container.register("non_singleton_service", factory, singleton=False)
        instance1 = self.container.resolve("non_singleton_service")
        instance2 = self.container.resolve("non_singleton_service")
        self.assertNotEqual(instance1, instance2)

    def test_missing_service(self):
        with self.assertRaises(ValueError):
            self.container.resolve("missing_service")

if __name__ == "__main__":
    unittest.main()
