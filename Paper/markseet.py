def total_subject(math , urdu, eng , sci , isl):
    obt =  math +  urdu + eng + sci +  isl
    return obt
def percentage(total):
    per = (obt /500) * 100    
    return per
def grade(per):
    if per >= 80:
        return "A+"
    elif per >= 70:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 50:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "F"
math = int(input("Enter marks obtained in Math: "))
urdu = int(input("Enter marks obtained in Urdu: "))
eng = int(input("Enter marks obtained in English: "))
sci = int(input("Enter marks obtained in Science: "))
isl = int(input("Enter marks obtained in Islamiat: "))

obt = total_subject(math , urdu, eng , sci , isl)
per = percentage(obt)
grd = grade(per)

print(f"Total Marks Obtained: {obt} out of 500")
print(f"Percentage: {per}%")
print(f"Grade: {grd}")

