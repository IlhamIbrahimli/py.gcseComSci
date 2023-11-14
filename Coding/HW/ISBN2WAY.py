num = input("Enter ISBN:")
num = num.replace("-","")
sumOfCalc = 0

for i in range(len(num)):
    if i+1 %2 == 0:
        sumOfCalc += int(num[i]) * 3
    else:
        sumOfCalc += int(num[i])

chckDigit = sumOfCalc % 10
if chckDigit != 0:
    chckDigit = 10-chckDigit
if chckDigit == int(num[-1]):
    print("Valid ISBN")
else:
    print("Invalid ISBN")



#GOOFYAHHWAY
num = input("Enter ISBN:")
num = num.replace("-","")
actualChkDigit = int(num[-1])
numList = [int(i) for i in list(num)[:-1]]
multipliers= [1 if j%2 == 0 else 3 for j in range(12)]
endList = [a*b for a,b in zip(numList,multipliers)]

sumOfCalc = sum(endList)


chckDigit = sumOfCalc % 10
if chckDigit != 0:
    chckDigit = 10-chckDigit
if chckDigit == actualChkDigit:
    print("Valid ISBN")
else:
    print("Invalid ISBN")
