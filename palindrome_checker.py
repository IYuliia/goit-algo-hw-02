from collections import deque

def is_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  
    return True 

if __name__ == "__main__":
    test_strings = [
    "level",   
    "Python",        
    "Madam, in Eden, I'm Adam",  
]
    
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' -> {'Паліндром' if result else 'Не паліндром'}")
