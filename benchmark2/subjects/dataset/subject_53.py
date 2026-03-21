def validate_lambda_expression(expression):
    try:
        parsed_expression = parse(expression)
        if not isinstance(parsed_expression, ComposedForm) or len(parsed_expression.elements) != 2:
            return False  # Lambda expression should have two elements: parameters and body

        parameters, body = parsed_expression.elements
        if not isinstance(parameters, list) or not all(isinstance(param, Param) for param in parameters):
            return False  # Parameters should be a list of Param objects

        for param in parameters:
            if not isinstance(param, Param) or not isinstance(param.variable, Variable) or param.variable.name not in ["int", "bool", "float"]:
                return False  # Each parameter should consist of a valid type and variable name

        if not isinstance(body, ComposedForm):
            return False  # Body of the lambda expression should be a valid Lispyc expression

        return True  # If all validation checks pass, the lambda expression is valid
    except Exception:
        return False  # Catch any parsing errors and return False