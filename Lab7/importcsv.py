import csv

companies = []
sales = []

with open('carSale.csv') as f:
    lines = f.readlines()

for x in range(0, len(lines), 2):
    companies.append(lines[x].strip())
    data = lines[x+1].strip().split(',')
    sales.append(list(map(int, data)))
    
monthly_sales = [0] * 8
yearly_sales = [0] * len(companies)

for i in range(len(sales[0])):
    for j in range(len(sales)):
        monthly_sales[i] += sales[j][i]
        
for i in range(len(sales)):
    yearly_sales[i] = sum(sales[i])
    
print(monthly_sales)
print()

for i in range(len(companies)):
    print(companies[i], yearly_sales[i])
    
print()    
print("Grand total: ", sum(yearly_sales))