import unittest

class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = TaskScheduler()

    def test_add_task(self):
        def dummy_action():
            pass
        self.scheduler.add_task("Test Task", 1.0, dummy_action)
        self.assertEqual(len(self.scheduler.tasks), 1)
        self.assertEqual(self.scheduler.tasks[0]["name"], "Test Task")
        self.assertEqual(self.scheduler.tasks[0]["interval"], 1.0)
        self.assertEqual(self.scheduler.tasks[0]["action"], dummy_action)

    def test_run_pending(self):
        def dummy_action():
            pass
        self.scheduler.add_task("Test Task", 0.001, dummy_action)
        self.scheduler.run_pending()
        self.assertEqual(len(self.scheduler.tasks), 1)
        self.assertEqual(self.scheduler.tasks[0]["name"], "Test Task")
        self.assertEqual(self.scheduler.tasks[0]["action"], dummy_action)

if __name__ == "__main__":
    unittest.main()
