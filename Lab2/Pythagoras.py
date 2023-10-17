print("Pythagoras' Calculator")
print("1. Find the length of A given B and C")  
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

choice = int(input("Enter choice (1-3): "))

if choice == 1:
    b = float(input("Enter length of B: "))
    c = float(input("Enter length of C: "))
    a = (c**2 - b**2)**0.5
    print("Length of A is", a)

elif choice == 2:
    a = float(input("Enter length of A: "))  
    c = float(input("Enter length of C: "))
    b = (c**2 - a**2)**0.5 
    print("Length of B is", b)

elif choice == 3:
    a = float(input("Enter length of A: "))
    b = float(input("Enter length of B: "))
    c = (a**2 + b**2)**0.5
    print("Length of C is", c)
    
else:
    print("Invalid choice")