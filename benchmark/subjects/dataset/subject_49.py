class RPNCalculator:
    def __init__(self):
        self.stack = []
        self.ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

    def evaluate(self, expression: str) -> float:
        for token in expression.split():
            if token in self.ops:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(self.ops[token](a, b))
            else:
                self.stack.append(float(token))
        return self.stack[0] if self.stack else 0.0