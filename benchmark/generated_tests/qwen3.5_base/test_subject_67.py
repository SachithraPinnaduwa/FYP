import unittest

class TestSnowflakeIdGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = SnowflakeIdGenerator(worker_id=1, datacenter_id=1)

    def test_initial_sequence(self):
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset(self):
        for _ in range(4096):
            self.generator.generate_id()
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_different_timestamp(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_datacenter_id(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.datacenter_id = 2
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_epoch(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.epoch = self.generator.epoch + 1
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        self.generator.epoch = self.generator.epoch + 1
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch_and_sequence(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        self.generator.epoch = self.generator.epoch + 1
        self.generator.sequence = 1
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch_and_sequence_and_last_timestamp(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        self.generator.epoch = self.generator.epoch + 1
        self.generator.sequence = 1
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch_and_sequence_and_last_timestamp_and_sequence(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        self.generator.epoch = self.generator.epoch + 1
        self.generator.sequence = 1
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        self.generator.sequence = 2
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch_and_sequence_and_last_timestamp_and_sequence_and_last_timestamp(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        self.generator.epoch = self.generator.epoch + 1
        self.generator.sequence = 1
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        self.generator.sequence = 2
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch_and_sequence_and_last_timestamp_and_sequence_and_last_timestamp_and_sequence(self):
        for _ in range(4096):
            self.generator.generate_id()
        self.generator.last_timestamp = self.generator.last_timestamp
        self.generator.worker_id = 2
        self.generator.datacenter_id = 2
        self.generator.epoch = self.generator.epoch + 1
        self.generator.sequence = 1
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        self.generator.sequence = 2
        self.generator.last_timestamp = self.generator.last_timestamp + 1
        self.generator.sequence = 3
        id1 = self.generator.generate_id()
        id2 = self.generator.generate_id()
        self.assertLess(id1, id2)

    def test_sequence_reset_with_same_timestamp_and_different_worker_id_and_datacenter_id_and_epoch_and_sequence_and_last_timestamp_and_sequence_and_last_timestamp