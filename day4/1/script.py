file = open('../input.txt', 'r')
Lines = file.readlines()

total = 0

for line in Lines:
    pairs = line.strip().split(',')

    starts = []
    ends = []

    for pair in pairs:
        range = pair.split('-')
        starts.append(int(range[0]))
        ends.append(int(range[1]))

    if (
        (
            starts[0] >= starts[1]
            and ends[0] <= ends[1]
        )
        or (
            starts[1] >= starts[0]
            and ends[1] <= ends[0]
        )
    ):
        total += 1

print(total)

