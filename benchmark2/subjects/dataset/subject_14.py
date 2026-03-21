def solve_expression(expr):
    try:
        return eval(expr)
    except Exception as e:
        return "The entered expression is invalid."