from typing import Dict

class MetricsRegistry:
    def __init__(self):
        self.counters: Dict[str, int] = {}
        self.gauges: Dict[str, float] = {}

    def inc_counter(self, name: str, value: int = 1):
        if name not in self.counters:
            self.counters[name] = 0
        self.counters[name] += value

    def set_gauge(self, name: str, value: float):
        self.gauges[name] = value

    def report(self) -> Dict[str, Dict[str, float]]:
        return {
            "counters": dict(self.counters),
            "gauges": dict(self.gauges)
        }