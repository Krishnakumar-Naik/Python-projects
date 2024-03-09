import string
import random
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("\n............................................\n")
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Enter a positive integer for password length.")
            return
        password = generate_password(length)
        print("Generated password is: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
if __name__ == "__main__":
    main()
