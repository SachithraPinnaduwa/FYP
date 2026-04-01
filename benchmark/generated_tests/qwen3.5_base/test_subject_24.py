import unittest

class TestStateMachine(unittest.TestCase):
    def setUp(self):
        self.sm = StateMachine("IDLE")

    def test_initial_state(self):
        self.assertEqual(self.sm.state, "IDLE")

    def test_add_transition(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.assertEqual(self.sm.state, "IDLE")

    def test_fire_transition(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")

    def test_invalid_transition(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.assertFalse(self.sm.fire("INVALID"))
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("IDLE", "PAUSED", "PAUSE")
        self.sm.add_transition("RUNNING", "PAUSED", "PAUSE")
        self.sm.add_transition("PAUSED", "RUNNING", "RESUME")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("PAUSE")
        self.assertEqual(self.sm.state, "PAUSED")
        self.sm.fire("RESUME")
        self.assertEqual(self.sm.state, "RUNNING")

    def test_multiple_transitions_from_same_state(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("IDLE", "PAUSED", "PAUSE")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("PAUSE")
        self.assertEqual(self.sm.state, "PAUSED")

    def test_multiple_transitions_to_same_state(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.add_transition("PAUSED", "IDLE", "RESUME")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("RESUME")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_from_same_state_to_different_states(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("IDLE", "PAUSED", "PAUSE")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.add_transition("PAUSED", "IDLE", "RESUME")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("PAUSE")
        self.assertEqual(self.sm.state, "PAUSED")
        self.sm.fire("RESUME")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_to_same_state_from_different_states(self):
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.add_transition("PAUSED", "IDLE", "RESUME")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("RESUME")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_from_same_state_to_same_state(self):
        self.sm.add_transition("IDLE", "IDLE", "NOOP")
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.fire("NOOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_to_same_state_from_same_state(self):
        self.sm.add_transition("IDLE", "IDLE", "NOOP")
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.fire("NOOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_from_same_state_to_same_state_from_different_states(self):
        self.sm.add_transition("IDLE", "IDLE", "NOOP")
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.add_transition("PAUSED", "IDLE", "RESUME")
        self.sm.fire("NOOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("RESUME")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_to_same_state_from_same_state_to_different_states(self):
        self.sm.add_transition("IDLE", "IDLE", "NOOP")
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "IDLE", "STOP")
        self.sm.add_transition("PAUSED", "IDLE", "RESUME")
        self.sm.fire("NOOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("START")
        self.assertEqual(self.sm.state, "RUNNING")
        self.sm.fire("STOP")
        self.assertEqual(self.sm.state, "IDLE")
        self.sm.fire("RESUME")
        self.assertEqual(self.sm.state, "IDLE")

    def test_multiple_transitions_from_same_state_to_same_state_from_same_state(self):
        self.sm.add_transition("IDLE", "IDLE", "NOOP")
        self.sm.add_transition("IDLE", "RUNNING", "START")
        self.sm.add_transition("RUNNING", "