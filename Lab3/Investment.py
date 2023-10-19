initial = 100
target = 1000
rate = 0.10 
years = 0
balance = initial
while balance < target:
  interest = balance * rate
  balance += interest  
  years += 1
print("It will take", years, "years for an initial £100 investment to grow to £1000 at 10% interest")