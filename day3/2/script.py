file = open('../input.txt', 'r')
Lines = file.readlines()

total = 0
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i, line in enumerate(Lines):
    # On every third line
    if (i+1) % 3 == 0:
        bag3 = line
        bag2 = Lines[i-1]
        bag1 = Lines[i-2]

        for c in bag1:
            if bag2.find(c) != -1 and bag3.find(c) != -1:
                total += letters.find(c) + 1
                break

print(total)

