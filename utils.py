import re
from errors import ImbalancedParanthesis


def areBracketsBalanced(text):
    stack = []
    for char in re.sub("[^()]", "", text):
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                raise ImbalancedParanthesis
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    raise ImbalancedParanthesis
    if stack:
        raise ImbalancedParanthesis
    else:
        return re.sub("[()]", "", text)
