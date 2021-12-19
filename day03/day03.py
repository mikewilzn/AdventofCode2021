zero = [0]*12
one = [0]*12

with open('input.txt') as my_file:
    for line in my_file:
        for i in range(len(line) - 1):
            if(line[i] == '0'):
                zero[i] += 1
            else:
                one[i] += 1

gamma = 0
epsilon = 0

for i in range(12):
    if(one[i] > zero[i]):
        gamma += 1 << 12 - i
    else:
        epsilon += 1 << 12 - i

print(gamma)
print(epsilon)