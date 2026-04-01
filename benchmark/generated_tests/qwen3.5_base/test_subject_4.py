import unittest

class TestThreadPoolWorker(unittest.TestCase):
    def setUp(self):
        self.pool = ThreadPoolWorker(num_threads=2)
        self.pool.start()

    def tearDown(self):
        self.pool.shutdown()

    def test_submit_and_get_results(self):
        task_id = "test_1"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        results = self.pool.get_results(block=True)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][2], 14)

    def test_submit_multiple_tasks(self):
        tasks = []
        for i in range(5):
            task_id = f"test_{i}"
            self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
            tasks.append(task_id)
        
        results = self.pool.get_results(block=True)
        self.assertEqual(len(results), 5)
        for result in results:
            self.assertEqual(result[2], 14)

    def test_submit_task_with_error(self):
        task_id = "test_error"
        def error_func():
            raise ValueError("Test error")
        
        self.pool.submit_task(task_id, error_func)
        results = self.pool.get_results(block=True)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], "error")
        self.assertEqual(results[0][2], "Test error")

    def test_submit_task_with_timeout(self):
        task_id = "test_timeout"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        results = self.pool.get_results(block=False, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_block(self):
        task_id = "test_timeout_block"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown(self):
        task_id = "test_timeout_shutdown"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=False)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait(self):
        task_id = "test_timeout_shutdown_wait"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block(self):
        task_id = "test_timeout_shutdown_wait_block"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout(self):
        task_id = "test_timeout_shutdown_wait_block_timeout"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block_timeout"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout_and_block(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block_timeout_block"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block_timeout_block_timeout"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout_and_block(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block_timeout_block_timeout_block"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block_timeout_block_timeout_block_timeout"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout_and_block(self):
        task_id = "test_timeout_shutdown_wait_block_timeout_block_timeout_block_timeout_block_timeout_block"
        self.pool.submit_task(task_id, cpu_bound_task, [1, 2, 3])
        self.pool.shutdown(wait=True)
        results = self.pool.get_results(block=True, timeout=0.1)
        self.assertEqual(len(results), 0)

    def test_submit_task_with_timeout_and_shutdown_and_wait_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout_and_block_and_timeout(self):
        task_id = "test_timeout_shutdown_wait_block