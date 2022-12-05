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
            starts[1] >= starts[0]
            and starts[1] <= ends[0]
        )
        or (
            starts[0] >= starts[1]
            and starts[0] <= ends[1]
        )
    ):
        total += 1

print(total)

