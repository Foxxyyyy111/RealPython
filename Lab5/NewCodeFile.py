import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
grades = data.split(',')

print(min(grades))
print(max(grades))

grades = list(map(int, grades))
print(grades)
max_grade = max(grades)
min_grade = min(grades)
print(min_grade) 
print(max_grade) 

total = sum(grades)
num_grades = len(grades)
avg = total / num_grades
avg = round(avg, 2)
print(avg)

meanavg = statistics.mean(grades)
meanavg = round(avg, 2)
print(meanavg)

medianavg = statistics.median(grades)
print(medianavg)

output = "max_grade:{}\nmin_grade:{}\navg:{}\nmeanavg:{}\nmedianavg:{}"
print(output.format(max_grade, min_grade, avg, meanavg, medianavg))