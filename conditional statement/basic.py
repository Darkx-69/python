a = int(input("Enter your age: "))
print(a < 18)

if 18 <= a <= 21:
    print("Eligible for young election")
elif a < 18:
    print("Not eligible to vote")
else:
    print("Not eligible")
