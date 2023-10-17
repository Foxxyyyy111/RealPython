exam_mark = int(input("Please enter your grade: "))
if exam_mark > 100:
  print("Error... Marks must be between 1 & 100")
elif exam_mark >= 71:
  print("Distinction")
elif exam_mark >= 61:  
  print("Merit")
elif exam_mark >= 50:
  print("Pass")
elif exam_mark < 50 and exam_mark > 1:
  print("Fail")  
elif exam_mark < 1:
  print("Error... Marks must be between 1 & 100")