f = open("input.txt", "r")
score = 0
sign_score = {"X" : 1, "Y" : 2, "Z" : 3, "A" : 1, "B" : 2, "C" : 3}

for line in f:
    opponent_sign, my_sign = line.split()
    my_score = sign_score[my_sign]
    opponent_score = sign_score[opponent_sign]
    score += my_score

    score_difference = my_score - opponent_score
    if score_difference:
        if score_difference == 1 or score_difference == -2:
                score += 6

    else: #draw
        score += 3

print(score)