import unittest

class TestSimpleDFA(unittest.TestCase):
    def test_empty_string(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertTrue(dfa.run(""))

    def test_single_char(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertTrue(dfa.run("ab"))
        self.assertFalse(dfa.run("a"))
        self.assertFalse(dfa.run("b"))

    def test_multiple_chars(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertTrue(dfa.run("abab"))
        self.assertFalse(dfa.run("ababab"))

    def test_invalid_transition(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        self.assertFalse(dfa.run("a"))

    def test_start_state_not_in_accepting(self):
        dfa = SimpleDFA("q0", {"q1"})
        dfa.add_transition("q0", "a", "q1")
        self.assertTrue(dfa.run("a"))

    def test_start_state_in_accepting(self):
        dfa = SimpleDFA("q0", {"q0"})
        self.assertTrue(dfa.run(""))

    def test_multiple_transitions_from_same_state(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q0", "b", "q2")
        self.assertTrue(dfa.run("a"))
        self.assertTrue(dfa.run("b"))

    def test_missing_transition(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        self.assertFalse(dfa.run("a"))

    def test_accepting_state_not_reached(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        self.assertFalse(dfa.run("a"))

    def test_accepting_state_reached(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q0")
        self.assertTrue(dfa.run("a"))

    def test_accepting_state_reached_multiple_times(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q0")
        self.assertTrue(dfa.run("aaaa"))

    def test_accepting_state_reached_multiple_times_with_different_transitions(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertTrue(dfa.run("abab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("ababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("abababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("ababababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("abababababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("ababababababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("abababababababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("ababababababababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("q0", {"q0"})
        dfa.add_transition("q0", "a", "q1")
        dfa.add_transition("q1", "b", "q0")
        self.assertFalse(dfa.run("abababababababababab"))

    def test_accepting_state_reached_multiple_times_with_different_transitions_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid_and_invalid(self):
        dfa = SimpleDFA("