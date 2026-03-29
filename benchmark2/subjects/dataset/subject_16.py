def solve_for_x(equation: str) -> int:
    from itertools import count
    
    # Iterate over positive and negative integers to find the value of x
    for n in count(0):
        for x in [n, -n]:
            # Replace 'x' with the current value of x and evaluate the equation
            if eval(equation.replace('x', str(x)).replace('=', '==')):
                return x