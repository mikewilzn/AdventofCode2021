numbers = []
with open('example.txt') as my_file:
    numbers = my_file.readlines()

bitCount = len(numbers[0]) - 1
zero = [0]*bitCount
one = [0]*bitCount

for line in numbers:
    for i in range(bitCount):
        if(line[i] == '0'):
            zero[i] += 1
        else:
            one[i] += 1

gamma = 0
epsilon = 0

for i in range(bitCount):
    if(one[i] > zero[i]):
        gamma += 1 << bitCount - i - 1
    else:
        epsilon += 1 << bitCount - i - 1

print(gamma * epsilon)

validOxygen = []
validCO2 = []

count = len(numbers)

while(count > 1):
    
for i in range(len(numbers)):
    if(zero[i] > one[i]):

        for number in numbers:
            if(number[i] == 0):