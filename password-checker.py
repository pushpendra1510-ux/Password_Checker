import re

def check_password_strength(password):
        # Check the length of the password
        if len(password) < 8: #length of Password 
                return "weak: password must be at least 8 char"
        
        if not any(char.isdigit() for char in password):
                return "weak: password must contain a digit"
                
        if not any(char.isupper() for char in password):
                return "weak: password must contain upper char"
        
        if not any(char.islower() for char in password):
                return "weak: password must contain lower char" # FIXED: Typo in message
                
        if not re.search(r'[!@#$%^&*(){}>?]', password): # FIXED: 'Password' changed to 'password'
                return "weak: password must contain a special char"
                
        return "strong: your password is secured!"

def password_checker():
        print("Welcome to the password strength checker")
        while True:
                password = input("Enter your password (or type 'exit' to quit): ")
                if password.lower() == 'exit':
                        print("Thank you for using this tool") # FIXED: Typo 'usnig'
                        break
                result = check_password_strength(password) # FIXED: Function name was spelled wrong
                print(result)

# Run the password checker tool 
if __name__ == "__main__":
        password_checker()