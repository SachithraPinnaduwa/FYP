def convert_to_camel_case(string):
    string = string.strip()
    result = ''
    capitalize_next = False

    for char in string:
        if char == ' ':
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char

    return result