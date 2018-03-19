# python3

"""If the code in text uses brackets correctly, output 'Success'. Otherwise,
output the 1-based index of the first unmatched closing bracket, 
and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket."""
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

def bracket_checker(text):
    """If the code in text uses brackets correctly, output 'Success'. 
    Otherwise, output the 1-based index of the first unmatched closing bracket, 
    and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
    examples:
    >>> bracket_checker('{')
    1
    >>> bracket_checker('}')
    1
    >>> bracket_checker('{[}')
    3
    >>> bracket_checker('}()')
    1
    >>> bracket_checker('{}[]')
    'Success'
    >>> bracket_checker('foo(bar[i)')
    10
    >>> bracket_checker('foo(bar)')
    'Success'
    """
    opening_brackets_stack = []
    for i, next in enumerate(text, 1): # index starts from 1
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
            
        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack == []:
                return i
                
            else:
                o = opening_brackets_stack.pop()
                if not o.Match(next):
                    return i                

    if opening_brackets_stack == []:
        return "Success"
    else:
        o = opening_brackets_stack.pop()
        return o.position
        
print(bracket_checker(text))
