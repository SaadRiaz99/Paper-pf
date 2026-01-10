
num = int(input("Enter a number: "))

# Even or Odd check
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

num = int(input("Enter check a prime number: "))

if num <= 1:
    print(f"{num} is neither prime nor composite.")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
