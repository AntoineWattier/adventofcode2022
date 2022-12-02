file = open('input.txt', 'r')
Lines = file.readlines()

score = 0

WIN = 6
TIE = 3
LOST = 0

# A/X: Rock
# B/Y: Paper
# C/Z: Scissors

bonus = { 'X': 1, 'Y': 2, 'Z': 3}
scoring = {
    'A' : {
        'X': TIE,
        'Y': WIN,
        'Z': LOST,
    },
    'B' : {
        'X': LOST,
        'Y': TIE,
        'Z': WIN,
    },
    'C' : {
        'X': WIN,
        'Y': LOST,
        'Z': TIE,
    },
}

for line in Lines:
    current_match = line.split()
    opponent = current_match[0]
    player = current_match[1]

    current_match_score = bonus[player] + scoring[opponent][player]

    print("Player:{} | Opponent:{} -> {} + {} -> {} ".format(player, opponent, bonus[player], scoring[opponent][player],  current_match_score))

    score += current_match_score

print(score)
