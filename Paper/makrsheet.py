

marks = {

}

def signup():
    email = input("Enter Your Email:")

    if email in marks:
        print("User Already Exist")
        return
    password = input("Enter The Password:")


    name = input("Student Name: ")
    roll = input("Roll Number: ")

    math = int(input("Math Marks: "))
    eng = int(input("English Marks: "))
    sci = int(input("Science Marks: "))

    total = math + eng + sci
    percentage = total / 3

    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

marks[email] = {
    "password": password,
        "name": name,
        "roll": roll,
        "math": math,
        "eng": eng,
        "sci": sci,
        "total": total,
        "percentage": percentage,
        "grade": grade
}
def login():
    email = input("Username: ")
    Password = input("Password: ")

    if email == marks and [email]["Password"] == password:
        print("Login successfully")

        show_marksheet(email)
    else:
        print("Invalid Email or Password")

# ---------- SHOW MARKSHEET ----------
def show_marksheet(email):
    s = marks[email]

    print(" MARKSHEET")
    print("-------------------")
    print("Name:", s["name"])
    print("Roll No:", s["roll"])
    print("Math:", s["math"])
    print("English:", s["eng"])
    print("Science:", s["sci"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"], "%")
    print("Grade:", s["grade"])
    print("-------------------")

# ---------- MENU ----------
while True:
    print("\n1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")