number = '9,223,372,036,854,775,807'
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))



x = 23
x-=4
print(x)

number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer+= number


print(number)
