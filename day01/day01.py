f = open('input.txt', 'r')

count = 0

previousLine = f.readline()

for line in f:
    if(line > previousLine):
        count += 1
    previousLine = line

print(count)
