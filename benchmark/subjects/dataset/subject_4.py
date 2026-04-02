def make_palindrome_by_insertion(s: str) -> str:
    def is_palindrome(n: str) -> bool:
        return n == n[::-1]
    
    for i in range(len(s) + 1):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            new_string = s[:i] + char + s[i:]
            if is_palindrome(new_string):
                return new_string
    
    return "NA"