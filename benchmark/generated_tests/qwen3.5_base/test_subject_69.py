import unittest

class TestJobQueue(unittest.TestCase):
    def setUp(self):
        self.job_queue = JobQueue(max_retries=2)

    def test_add_job(self):
        self.job_queue.add_job("job1", {"task": "test"})
        self.assertEqual(len(self.job_queue.queue), 1)

    def test_process_success(self):
        self.job_queue.add_job("job1", {"task": "test"})
        self.job_queue.process_next(lambda data: True)
        self.assertIn("job1", self.job_queue.completed)

    def test_process_failure(self):
        self.job_queue.add_job("job1", {"task": "test"})
        self.job_queue.process_next(lambda data: False)
        self.assertIn("job1", self.job_queue.failed)

    def test_max_retries(self):
        self.job_queue.add_job("job1", {"task": "test"})
        self.job_queue.process_next(lambda data: False)
        self.job_queue.process_next(lambda data: False)
        self.assertIn("job1", self.job_queue.failed)

    def test_empty_queue(self):
        self.assertFalse(self.job_queue.process_next(lambda data: True))

if __name__ == "__main__":
    unittest.main()
