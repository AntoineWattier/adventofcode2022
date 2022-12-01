# Loop through all lines
# Sum, stop on empty line or end
# Compare to previous highest, keep if higher

file = open('../input.txt', 'r')
Lines = file.readlines()

count = 0
highest = 0
current = 0

for line in Lines:
    count += 1

    if line.strip() == "" or Lines.count == count:
        print("Highest:{} | Current:{}".format(highest, current))
        if current > highest:
            highest = current

        current = 0
    else:
        current += int(line.strip())

print(highest)
