import re

class PasswordPolicyValidator:
    def __init__(self, min_length=8, req_upper=True, req_lower=True, req_num=True, req_special=True):
        self.min_length = min_length
        self.req_upper = req_upper
        self.req_lower = req_lower
        self.req_num = req_num
        self.req_special = req_special

    def validate(self, password: str) -> dict:
        errors = []
        if len(password) < self.min_length:
            errors.append(f"Must be at least {self.min_length} characters")
        if self.req_upper and not re.search(r'[A-Z]', password):
            errors.append("Must contain uppercase")
        if self.req_lower and not re.search(r'[a-z]', password):
            errors.append("Must contain lowercase")
        if self.req_num and not re.search(r'\d', password):
            errors.append("Must contain number")
        if self.req_special and not re.search(r'[^A-Za-z0-9]', password):
            errors.append("Must contain special character")
            
        return {
            "is_valid": len(errors) == 0,
            "errors": errors
        }