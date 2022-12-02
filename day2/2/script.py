file = open('input.txt', 'r')
Lines = file.readlines()

score = 0

WIN = 6
TIE = 3
LOST = 0

# A: Rock
# B: Paper
# C: Scissors

# X: LOSE
# Y: DRAW
# Z: WIN

bonus = { 'A': 1, 'B': 2, 'C': 3}
expected = { 'X': LOST, 'Y': TIE, 'Z': WIN}
scoring = {
    'A' : {
        'A': TIE,
        'B': WIN,
        'C': LOST,
    },
    'B' : {
        'A': LOST,
        'B': TIE,
        'C': WIN,
    },
    'C' : {
        'A': WIN,
        'B': LOST,
        'C': TIE,
    },
}

for line in Lines:
    current_match = line.split()
    opponent = current_match[0]

    # This will return X, Y, Z
    result = current_match[1]

    # This will return LOST, TIE, WIN
    expected_result = expected[result]

    # This will return A, B, C
    player = list(scoring[opponent].keys())[list(scoring[opponent].values()).index(expected_result)]

    current_match_score = expected_result + bonus[player]

    print("Player:{} | Opponent:{} -> {} + {} -> {} ".format(player, opponent, expected_result, bonus[player], current_match_score))

    score += current_match_score

print(score)
