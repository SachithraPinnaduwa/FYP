import unittest

class TestEventEmitter(unittest.TestCase):
    def setUp(self):
        self.eventEmitter = EventEmitter()

    def test_on(self):
        self.eventEmitter.on('test', lambda: None)
        self.assertEqual(len(self.eventEmitter.events['test']), 1)

    def test_emit(self):
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_emit_nonexistent(self):
        self.assertFalse(self.eventEmitter.emit('nonexistent'))

    def test_multiple_callbacks(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))
        self.assertTrue(self.eventEmitter.emit('test'))

    def test_multiple_callbacks_multiple_events(self):
        self.eventEmitter.on('test', lambda: None)
        self.eventEmitter.on('test', lambda: None)
        self.assertTrue(self.eventEmitter.emit('test'))