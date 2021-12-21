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

print("Power Consumption: " + str(gamma * epsilon))


##### Part 2 ######

def get_oxygen_criteria(array, check_bit):
    zeros = 0
    ones = 0
    for num in array:
        if(int(num[check_bit]) == 0):
            zeros += 1
        else:
            ones += 1
    return 1 if ones >= zeros else 0

def get_co2_criteria(array, check_bit):
    zeros = 0
    ones = 0
    for num in array:
        if(int(num[check_bit]) == 0):
            zeros += 1
        else:
            ones += 1
    return 1 if ones < zeros else 0


def get_oxygen_rating(remaining_numbers, check_bit):
    if(len(remaining_numbers) == 1):
        return remaining_numbers[0]
    else:
        new_array = []
        bit_criteria = get_oxygen_criteria(remaining_numbers, check_bit)
        for num in remaining_numbers:
            if(int(num[check_bit]) == bit_criteria):
                new_array.append(num)
        return get_oxygen_rating(new_array, check_bit + 1)

def get_co2_rating(remaining_numbers, check_bit):
    if(len(remaining_numbers) == 1):
        return remaining_numbers[0]
    else:
        new_array = []
        bit_criteria = get_co2_criteria(remaining_numbers, check_bit)
        for num in remaining_numbers:
            if(int(num[check_bit]) == bit_criteria):
                new_array.append(num)
        return get_co2_rating(new_array, check_bit + 1)

oxygen_rating = int(get_oxygen_rating(numbers, 0), 2)
co2_rating = int(get_co2_rating(numbers, 0), 2)

print("Life support rating: " + str(oxygen_rating * co2_rating))