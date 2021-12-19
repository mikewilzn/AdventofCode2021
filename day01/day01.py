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
print(count)
