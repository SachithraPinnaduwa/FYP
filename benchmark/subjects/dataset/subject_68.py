class SimpleDFA:
    def __init__(self, start_state: str, accepting_states: set):
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.transitions = {}

    def add_transition(self, src: str, char: str, dst: str):
        if src not in self.transitions:
            self.transitions[src] = {}
        self.transitions[src][char] = dst

    def run(self, input_string: str) -> bool:
        current = self.start_state
        for char in input_string:
            if current not in self.transitions or char not in self.transitions[current]:
                return False
            current = self.transitions[current][char]
        return current in self.accepting_states