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

parentheses_string = input("Enter a string with parentheses: ")

if is_valid_parentheses(parentheses_string):
    print("Valid parentheses")
else:
    print("Not valid parentheses")
