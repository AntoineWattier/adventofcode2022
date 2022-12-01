# Loop through all lines
# Sum, stop on empty line or end
# Add to array
# Sort array
# Sum top 3

file = open('../input.txt', 'r')
Lines = file.readlines()

count = 0
current = 0
array = []

for line in Lines:
    count += 1

    if line.strip() == "" or Lines.count == count:
        array.append(current)
        current = 0
    else:
        current += int(line.strip())

array.sort(reverse=True)

print(sum(array[:3]))
