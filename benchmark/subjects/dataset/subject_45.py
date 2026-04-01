import math

class StandardDeviationCalc:
    def __init__(self, data: list):
        self.data = data
        self.mean = sum(data) / len(data) if data else 0.0

    def compute_variance(self) -> float:
        if not self.data:
            return 0.0
        return sum((x - self.mean) ** 2 for x in self.data) / len(self.data)

    def compute_std_dev(self) -> float:
        return math.sqrt(self.compute_variance())