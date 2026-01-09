Data = []

def Signup():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Error: Passwords do not match.")
        return False
    else:
        Data.append((email, password))
        print(f"Signup successful for {email}!")
        return True

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user_email, user_password in Data:
        if email == user_email and password == user_password:
            print("Login successful!")
            return

    print("Error: Invalid email or password.")


print(" 1 for Signup \n 2 for Login")
choice = int(input("Enter your choice: "))
if choice == 1:

    Signup()
elif choice == 2:

    login()
else:
    print("Invalid choice.")    
