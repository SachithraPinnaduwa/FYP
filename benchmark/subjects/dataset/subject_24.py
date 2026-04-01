class StateMachine:
    def __init__(self, initial_state: str):
        self.state = initial_state
        self.transitions = {}

    def add_transition(self, from_state: str, to_state: str, trigger: str):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][trigger] = to_state

    def fire(self, trigger: str) -> bool:
        if self.state in self.transitions and trigger in self.transitions[self.state]:
            self.state = self.transitions[self.state][trigger]
            return True
        return False