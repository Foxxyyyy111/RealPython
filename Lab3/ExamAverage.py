math_mark = int(input("Enter math mark: "))
english_mark = int(input("Enter english mark: "))  
ict_mark = int(input("Enter ICT mark: "))

if math_mark < 1 or math_mark > 100:
  print("Math mark error")
if english_mark < 1 or english_mark > 100:
  print("English mark error")
if ict_mark < 1 or ict_mark > 100:
  print("ICT mark error")
  
average = (int(math_mark) + int(english_mark) + int(ict_mark)) / 3

print(average)

if average >= 65:
  print("Pass")
else: 
  print("Fail")