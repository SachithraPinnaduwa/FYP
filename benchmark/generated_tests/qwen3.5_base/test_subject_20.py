import unittest

class TestDebouncer(unittest.TestCase):
    def setUp(self):
        self.debounce = Debouncer(0.1)
        self.counter = 0

    def test_basic_debounce(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment)
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_cancel_debounce(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment)
        self.debounce.cancel()
        time.sleep(0.2)
        self.assertEqual(counter, 0)

    def test_multiple_debounces(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment)
        time.sleep(0.05)
        self.debounce(increment)
        time.sleep(0.15)
        self.assertEqual(counter, 1)

    def test_debounce_with_kwargs(self):
        def greet(name):
            return f"Hello, {name}!"

        self.debounce(greet, name="World")
        time.sleep(0.2)
        self.assertEqual(greet("World"), "Hello, World!")

    def test_debounce_with_args(self):
        def add(a, b):
            return a + b

        self.debounce(add, 1, 2)
        time.sleep(0.2)
        self.assertEqual(add(1, 2), 3)

    def test_debounce_with_kwargs_and_args(self):
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        self.debounce(greet, "World", greeting="Hi")
        time.sleep(0.2)
        self.assertEqual(greet("World", greeting="Hi"), "Hi, World!")

    def test_debounce_with_exception(self):
        def divide(a, b):
            return a / b

        self.debounce(divide, 1, 0)
        time.sleep(0.2)
        self.assertEqual(divide(1, 0), 0)

    def test_debounce_with_threading(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment)
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_multiple_threads(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment)
        self.debounce(increment)
        self.debounce(increment)
        time.sleep(0.3)
        self.assertEqual(counter, 1)

    def test_debounce_with_long_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=1.0)
        time.sleep(1.1)
        self.assertEqual(counter, 1)

    def test_debounce_with_short_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=0.01)
        time.sleep(0.02)
        self.assertEqual(counter, 1)

    def test_debounce_with_zero_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=0.0)
        time.sleep(0.01)
        self.assertEqual(counter, 1)

    def test_debounce_with_negative_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=-1.0)
        time.sleep(0.01)
        self.assertEqual(counter, 1)

    def test_debounce_with_none_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=None)
        time.sleep(0.01)
        self.assertEqual(counter, 1)

    def test_debounce_with_string_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time="0.1")
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_list_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=[0.1])
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_tuple_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=(0.1,))
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_dict_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time={"wait_time": 0.1})
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_set_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time={0.1})
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_frozen_set_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=frozenset({0.1}))
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_generator_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=(x for x in [0.1]))
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_iterator_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=iter([0.1]))
        time.sleep(0.2)
        self.assertEqual(counter, 1)

    def test_debounce_with_iterator_wait_time(self):
        def increment():
            nonlocal counter
            counter += 1
            return counter

        self.debounce(increment, wait_time=iter([0.1]))
        time.sleep(0.