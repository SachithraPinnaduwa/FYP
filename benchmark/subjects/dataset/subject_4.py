import threading
import time
import queue
from typing import Any, Callable

def cpu_bound_task(data: list) -> int:
    return sum(d * d for d in data)

class ThreadPoolWorker:
    """A realistic implementation of a simple thread pool and worker queue."""
    def __init__(self, num_threads: int = 4):
        self.num_threads = num_threads
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.workers = []
        self.is_running = False

    def start(self):
        if self.is_running:
            return
            
        self.is_running = True
        for _ in range(self.num_threads):
            t = threading.Thread(target=self._worker_loop, daemon=True)
            self.workers.append(t)
            t.start()

    def _worker_loop(self):
        while self.is_running:
            try:
                task_id, func, args, kwargs = self.task_queue.get(timeout=0.5)
            except queue.Empty:
                continue
                
            try:
                result = func(*args, **kwargs)
                self.result_queue.put((task_id, "success", result))
            except Exception as e:
                self.result_queue.put((task_id, "error", str(e)))
            finally:
                self.task_queue.task_done()

    def submit_task(self, task_id: str, func: Callable, *args, **kwargs) -> bool:
        if not self.is_running:
            return False
        self.task_queue.put((task_id, func, args, kwargs))
        return True

    def get_results(self, block: bool = True, timeout: float = None) -> list:
        results = []
        try:
            while not self.result_queue.empty() if not block else True:
                results.append(self.result_queue.get(block=block, timeout=timeout))
                if len(results) >= self.result_queue.qsize():
                    break
        except queue.Empty:
            pass # Timeout hit or queue emptied
        return results

    def shutdown(self, wait: bool = True):
        self.is_running = False
        if wait:
            for w in self.workers:
                w.join()
        self.workers.clear()
        
