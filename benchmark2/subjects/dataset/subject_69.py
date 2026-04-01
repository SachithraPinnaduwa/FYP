from collections import deque

class JobQueue:
    def __init__(self, max_retries: int = 3):
        self.queue = deque()
        self.max_retries = max_retries
        self.completed = []
        self.failed = []

    def add_job(self, job_id: str, payload: dict):
        self.queue.append({"id": job_id, "data": payload, "retries": 0})

    def process_next(self, processor_func) -> bool:
        if not self.queue:
            return False
            
        job = self.queue.popleft()
        try:
            success = processor_func(job["data"])
            if success:
                self.completed.append(job["id"])
            else:
                self._handle_failure(job)
        except Exception:
            self._handle_failure(job)
            
        return True

    def _handle_failure(self, job: dict):
        job["retries"] += 1
        if job["retries"] < self.max_retries:
            self.queue.append(job)
        else:
            self.failed.append(job["id"])