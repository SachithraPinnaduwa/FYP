from datetime import datetime, timedelta

class TimeSeriesAggregator:
    def __init__(self):
        self.data = []

    def add_point(self, timestamp: datetime, value: float):
        self.data.append({"ts": timestamp, "val": value})

    def aggregate_by_day(self) -> dict:
        results = {}
        for point in self.data:
            day_str = point["ts"].strftime("%Y-%m-%d")
            if day_str not in results:
                results[day_str] = {"sum": 0.0, "count": 0, "min": point["val"], "max": point["val"]}
                
            results[day_str]["sum"] += point["val"]
            results[day_str]["count"] += 1
            if point["val"] < results[day_str]["min"]:
                results[day_str]["min"] = point["val"]
            if point["val"] > results[day_str]["max"]:
                results[day_str]["max"] = point["val"]
                
        for day in results:
            results[day]["avg"] = results[day]["sum"] / results[day]["count"]
            
        return results