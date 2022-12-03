file = open('../input.txt', 'r')
Lines = file.readlines()

total = 0
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in Lines:
    middle = int(len(line.strip()) / 2)
    bag1 = line[:middle]
    bag2 = line[middle:]

    for c in bag1:
        if bag2.find(c) != -1:
            total += letters.find(c) + 1
            break

print(total)

