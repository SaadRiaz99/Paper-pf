data = [

]
def Signup():
    email = str(input("Enter Your Email:"))
    password = str(input("Enter Your password:"))
    confirm_password = str(input("Enter Your password Again:"))

    if password != confirm_password:
        print("Enter Your Corect Passwords")
        return False
    else:
        
        data.append((email , password))
        print(f"successful Login {email}")
        return True
        
def login():
    email = str(input("Enter Your Email:"))
    password = str(input("Enter Your password:"))
    
    for user_email, user_password in data:
        if email == user_email and password == user_password:
            print("successful Login:")
            return

        
    print("Error")
print(" 1 for Signup \n 2 for Login")
choice = int(input("Enter your choice: "))
if choice == 1:

    Signup()
elif choice == 2:

    login()
else:
    print("Invalid choice.")    
            