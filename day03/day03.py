numbers = []
with open('example.txt') as my_file:
    numbers = my_file.readlines()

bit_count = len(numbers[0]) - 1
zero = [0]*bit_count
one = [0]*bit_count

for line in numbers:
    for i in range(bit_count):
        if(line[i] == '0'):
            zero[i] += 1
        else:
            one[i] += 1

gamma = 0
epsilon = 0

for i in range(bit_count):
    if(one[i] > zero[i]):
        gamma += 1 << bit_count - i - 1
    else:
        epsilon += 1 << bit_count - i - 1

print(gamma * epsilon)


##### Part 2 ######

oxygen_criteria = []
for i in range(len(zero)):
    if(one[i] >= zero[i]):
        oxygen_criteria.append(1)
    else:
        oxygen_criteria.append(0)

oxygen_matches = [0]*len(numbers)

print("Oxygen criteria: " + str(oxygen_criteria))

for i in range(len(numbers)):
    for j in range(len(numbers[i])-1):
        if(int(numbers[i][j]) == oxygen_criteria[j]):
            oxygen_matches[i] += 1
        else:
            break

print("Oxygen matches: " + str(oxygen_matches))

co2_criteria = []
for i in range(len(zero)):
    if(one[i] < zero[i]):
        co2_criteria.append(1)
    else:
        co2_criteria.append(0)

co2_matches = [0]*len(numbers)

for number in numbers:
    for i in range(len(number)):
        if(number[i] == co2_criteria[i]):
            co2_matches[i] += 1
        else:
            break

print("Oxygen rating: " + numbers[max(oxygen_matches)])
print("CO2 rating: " + numbers[max(co2_matches)])