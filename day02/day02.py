position = 0
depth = 0

######## Part 1 ########
with open('input.txt') as my_file:
    for line in my_file:
        arguments = line.split(' ')
        instruction = arguments[0]
        value = int(arguments[1])
        
        if(instruction == 'forward'):
            position += value
        elif(instruction == 'down'):
            depth += value
        elif(instruction == 'up'):
            depth -= value
        else:
            print("Invalid instruction")

print("Part 1:")
print("Position: " + str(position))
print("Depth: " + str(depth))
print("Product: " + str(position * depth))

######## Part 2 ########
aim = 0
position = 0
depth = 0

with open('input.txt') as my_file:
    for line in my_file:
        arguments = line.split(' ')
        instruction = arguments[0]
        value = int(arguments[1])

        if(instruction == 'forward'):
            position += value
            depth += aim * value
        elif(instruction == 'down'):
            aim += value
        elif(instruction == 'up'):
            aim -= value
        else:
            print("Invalid instruction")

print("Part 2:")
print("Position: " + str(position))
print("Depth: " + str(depth))
print("Product: " + str(position * depth))