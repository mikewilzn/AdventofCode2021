from math import inf

inputs = []
with open('input.txt') as my_file:
    for line in my_file:
        inputs.append(int(line))

count = 0
previousDepth = inputs[0]
for i in inputs[1:]:
    if(i > previousDepth):
        count += 1
    previousDepth = i
print("Part One: " + str(count))

previousWindow = inf
count = 0

for i in range(2, len(inputs)):
    window = sum(inputs[i - 2 : i + 1])
    if(window > previousWindow):
        count += 1
    previousWindow = window
print("Part Two: " + str(count))
