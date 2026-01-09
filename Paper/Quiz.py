import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Marksheet")
root.geometry("400x450")

def result():
    try:
        s_name = name.get()
        s_roll = roll.get()

        eng = int(english.get())
        ur = int(urdu.get())
        sci = int(science.get())
        mat = int(maths.get())
    except:
        messagebox.showerror("Invalid Input", "Please enter valid data")
        return

    total = eng + ur + sci + mat
    percentage = (total / 400) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    messagebox.showinfo(
        "Result",
        f"Name: {s_name}\n"
        f"Roll No: {s_roll}\n"
        f"Total Marks: {total}\n"
        f"Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}"
    )
label_bg = "#eaf2f8"
tk.Label(root, text="Student Marksheet" , fg="red", font=("Arial", 14, "bold") , bg = label_bg ).grid(
    row=0, column=0, columnspan=2, pady=15
)

# Labels & Entries
tk.Label(root, text="Student Name").grid(row=1, column=0, padx=10, pady=5, sticky="w")
name = tk.Entry(root)
name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Roll No").grid(row=2, column=0, padx=10, pady=5, sticky="w")
roll = tk.Entry(root)
roll.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="English").grid(row=3, column=0, padx=10, pady=5, sticky="w")
english = tk.Entry(root)
english.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Urdu").grid(row=4, column=0, padx=10, pady=5, sticky="w")
urdu = tk.Entry(root)
urdu.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Science").grid(row=5, column=0, padx=10, pady=5, sticky="w")
science = tk.Entry(root)
science.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Maths").grid( row=6, column=0, padx=10, pady=5, sticky="w")
maths = tk.Entry(root)
maths.grid(row=6, column=1, padx=10, pady=5 )

# Buttons
tk.Button(root, text="Show Result", command=result).grid(
    row=7, column=0, padx=10, pady=20
)

tk.Button(root, text="Exit", command=root.destroy).grid(
    row=7, column=1, padx=10, pady=20
)

root.mainloop()