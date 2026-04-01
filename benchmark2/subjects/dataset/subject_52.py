class SimpleRegexMatcher:
    def match(self, pattern: str, text: str) -> bool:
        if not pattern:
            return not text
            
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.match(pattern[2:], text) or 
                    (first_match and self.match(pattern, text[1:])))
        else:
            return first_match and self.match(pattern[1:], text[1:])