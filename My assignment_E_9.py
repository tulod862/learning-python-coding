
def is_palindrome(s):

    s = s.lower()
    filtered_s = ''.join(char for char in s if char.isalnum())

    left=0
    right=len(filtered_s)-1

    while left < right:
        if filtered_s[left]!= filtered_s[right]:
    
             return False
        left+=1
        right-=1

    return True
    
def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
