import time

class SnowflakeIdGenerator:
    def __init__(self, worker_id: int, datacenter_id: int, epoch: int = 1609459200000):
        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.epoch = epoch
        self.sequence = 0
        self.last_timestamp = -1

    def _get_time(self):
        return int(time.time() * 1000)

    def generate_id(self) -> int:
        timestamp = self._get_time()

        if timestamp < self.last_timestamp:
            raise ValueError("Clock moved backwards")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & 4095
            if self.sequence == 0:
                while timestamp <= self.last_timestamp:
                    timestamp = self._get_time()
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        return ((timestamp - self.epoch) << 22) | \
               (self.datacenter_id << 17) | \
               (self.worker_id << 12) | \
               self.sequence