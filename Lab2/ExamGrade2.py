print("Enter exam mark (1-100): ")
mark = int(input())

if mark < 1 or mark > 100:
    print("Error: marks must be between 1 and 100")
else:
    print("Enter level (1 or 2): ")  
    level = int(input())
    
    if level == 1:
        if mark < 50:
            print("Fail")
        elif mark >= 50 and mark <= 60:
            print("Pass") 
        elif mark >= 61 and mark <= 70:
            print("Merit")
        else:
            print("Distinction")

    elif level == 2:
        if mark < 40:
            print("Fail")
        elif mark >= 40 and mark <= 50:
            print("Pass")
        elif mark >= 51 and mark <= 65: 
            print("Merit")
        else:
            print("Distinction")