import string
import random

def generate_password(leng):
   
    char = string.ascii_letters + string.digits + string.punctuation
    
  
    password = ''.join(random.choice(char) for i in range(leng))
    
    return password

def main():
  
    try:
        length = int(input("Enter the desired length for your password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    password = generate_password(length)
    
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
