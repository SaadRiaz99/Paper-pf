Data = []

def Signup():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    # check email already exists
    for user_email, _ in Data:
        if email == user_email:
            print("Error: Email already registered.")
            return

    if password != confirm_password:
        print("Error: Passwords do not match.")
    else:
        Data.append((email, password))
        print(f"Signup successful for {email}!")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    for user_email, user_password in Data:
        if email == user_email and password == user_password:
            print("Login successful!")
            return

    print("Error: Invalid email or password.")

print("1 for Signup")
print("2 for Login")

choice = int(input("Enter your choice: "))

if choice == 1:
    Signup()
elif choice == 2:
    login()
else:
    print("Invalid choice.")
