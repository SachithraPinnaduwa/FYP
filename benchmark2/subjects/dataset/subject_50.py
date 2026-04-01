class CSVParser:
    def __init__(self, delimiter: str = ',', quotechar: str = '"'):
        self.delimiter = delimiter
        self.quotechar = quotechar

    def parse_line(self, line: str) -> list:
        result = []
        current = []
        in_quotes = False
        
        for char in line:
            if char == self.quotechar:
                in_quotes = not in_quotes
            elif char == self.delimiter and not in_quotes:
                result.append(''.join(current))
                current = []
            else:
                current.append(char)
                
        result.append(''.join(current))
        return result