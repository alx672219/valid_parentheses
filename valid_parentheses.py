def isValid(self, s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = {"(", "[", "{"}
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:   # find corresponding closing parentheses
                stack.pop()
        else:
            return False
    return stack == []