numb = int(input("Enter the Number:"))

if numb % 2  == 0 :
    print("Number is Even")
else:
    print("Number is odd")    
numb = int(input("Enter the Number:"))

if numb <= 1:
    print("Number is not prime or either")
else:
    for i in range(2, numb):
        if numb % i == 0:
            print("This number is not prime")
            break
        else:
            print("Number is prime")

