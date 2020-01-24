
number= "9,231,562,767,789,064"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ("not pinin'", "no more", "a stiff", "bereft of life"):
    print("This parrot is "+ state)

for i in range(0,100, 5):
    print("i is {} ".format(i))

for j in range(1,13):
    for i in range(1,13):
        print("{1} times {0} is {2}   ".format(i,j, i*j), end='\t')
    #print("===========")
    print('')

for i in range(0, 101, 7):
    print(i)

