import time

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name: str, interval: float, action):
        self.tasks.append({
            "name": name,
            "interval": interval,
            "action": action,
            "next_run": time.time() + interval
        })

    def run_pending(self):
        now = time.time()
        for task in self.tasks:
            if now >= task["next_run"]:
                task["action"]()
                task["next_run"] = now + task["interval"]