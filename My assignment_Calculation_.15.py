def calculate_expression(expression):
    
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

def main():
    
    print("Welcome to the simple calculator.")
    
    while True:

        user_input = input("Enter a calculation (e.g., 45+2) or 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            break
        
        result = calculate_expression(user_input)
        print(f"Output is: {result}")

if __name__ == "_main_":main()