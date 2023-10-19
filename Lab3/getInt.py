min_val = 1
max_val = 100
attempts = 0
while attempts < 3:
  val = input("Enter an integer between 1 and 100" + str(min_val) + " and " + str(max_val) + ": ")

  try:
    val = int(val)
    if min_val <= val <= max_val:
      break
    elif:
      print("Number must be between " + str(min_val) + " and " + str(max_val))
    else:
    print("Invalid input. Please enter an integer.")  

  attempts += 1
if attempts == 3:
  print("None")
else:
  print("You entered:", val)