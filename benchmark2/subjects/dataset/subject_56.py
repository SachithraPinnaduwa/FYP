import datetime

class SystemHealthChecker:
    def __init__(self, cpu_thresh: float = 80.0, mem_thresh: float = 85.0):
        self.cpu_thresh = cpu_thresh
        self.mem_thresh = mem_thresh
        self.records = []

    def record_metrics(self, cpu: float, memory: float, disk: float):
        timestamp = datetime.datetime.now()
        status = "HEALTHY"
        if cpu > self.cpu_thresh or memory > self.mem_thresh:
            status = "WARNING"
            if cpu > 95.0 or memory > 95.0:
                status = "CRITICAL"
                
        self.records.append({
            "time": timestamp,
            "cpu": cpu,
            "memory": memory,
            "disk": disk,
            "status": status
        })

    def get_latest_status(self) -> str:
        if not self.records:
            return "UNKNOWN"
        return self.records[-1]["status"]

    def alert_needed(self) -> bool:
        if len(self.records) < 3:
            return False
        return all(r["status"] in ["WARNING", "CRITICAL"] for r in self.records[-3:])