def is_valid_parentheses(s):
    
    count = 0
    for char in s:
        if char == "(":
            count += 1 
        elif char == ")":
            count -= 1 
            if count < 0:  
                return False
    return count == 0  

def is_valid_brackets(s):

    brackets = []
    matches = {')': '(', ']': '['}
    for char in s:
        if char in '([':
            brackets.append(char)
        elif char in ')]':
            if not brackets or brackets[-1] != matches[char]:
                return False
            brackets.pop()
    
    return not brackets


parentheses_string = input("Enter string with parentheses: ")
print("Valid parentheses" if is_valid_parentheses(parentheses_string) else "Not valid parentheses")

brackets_string = input("Enter string with parentheses and brackets: ")
print("Valid" if is_valid_brackets(brackets_string) else "Not valid")