total = 0
for i in range(10):
    total += i

print(total)

#Modified

total = 0
for i in range(1,101):
    total += i
print(total)

#Make
timesTable = int(input("Enter a number:"))

for i in range(1,13):
    print(f'{i}x{timesTable} = {i*timesTable}')