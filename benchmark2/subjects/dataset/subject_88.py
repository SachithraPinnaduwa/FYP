class ShuntingYard:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

    def infix_to_postfix(self, expression: str) -> str:
        output = []
        operators = []
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()

        for token in tokens:
            if token.isnumeric() or token.replace('.', '', 1).isdigit():
                output.append(token)
            elif token in self.precedence:
                while (operators and operators[-1] != '(' and
                       (self.precedence.get(operators[-1], 0) > self.precedence[token] or
                        (self.precedence.get(operators[-1], 0) == self.precedence[token] and
                         self.associativity[token] == 'L'))):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if operators and operators[-1] == '(':
                    operators.pop()

        while operators:
            output.append(operators.pop())

        return " ".join(output)