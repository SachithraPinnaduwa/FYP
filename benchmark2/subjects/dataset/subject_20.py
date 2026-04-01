import time
import threading

class Debouncer:
    def __init__(self, wait_time: float):
        self.wait_time = wait_time
        self.timer = None

    def __call__(self, fn, *args, **kwargs):
        if self.timer is not None:
            self.timer.cancel()
        self.timer = threading.Timer(self.wait_time, fn, args=args, kwargs=kwargs)
        self.timer.start()
        
    def cancel(self):
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None