def day02_1():
    file = open("Day_02/input")
    score = 0
    val = [[],[]]
#Rock Paper Scissors
    for x in file:
        if x[0] == "A":
            val[1].append(1)
        if x[0] == "B":
            val[1].append(2)
        if x[0] == "C":
            val[1].append(3)
        if x[2] == "X":
            val[0].append(1)
        if x[2] == "Y":
            val[0].append(2)
        if x[2] == "Z":
            val[0].append(3)
    for x in range(len(val[0])):

        if val[0][x] == val[1][x]:
            score += val[0][x] + 3
        elif val[0][x] == val[1][x]+1 or val[0][x] == val[1][x]-2:
            score += val[0][x] + 6
        else:
            score += val[0][x]


    return score


def day02_1():
    file = open("Day_02/input")
    score = 0
    val = [[],[]]
#Rock Paper Scissors
    for x in file:
        if x[0] == "A":
            val[1].append(1)
        if x[0] == "B":
            val[1].append(2)
        if x[0] == "C":
            val[1].append(3)
        if x[2] == "X":
            if val[1][-1] == 1:
                val[0].append(3)
            else:
                val[0].append(val[1][-1]-1)
        if x[2] == "Y":
            val[0].append(val[1][-1])
        if x[2] == "Z":
            if val[1][-1] == 3:
                val[0].append(1)
            else:
               val[0].append(val[1][-1]+1)
        print(val[0][:10],val[1][:10])
    for x in range(len(val[0])):

        if val[0][x] == val[1][x]:
            score += val[0][x] + 3
        elif val[0][x] == val[1][x]+1 or val[0][x] == val[1][x]-2:
            score += val[0][x] + 6
        else:
            score += val[0][x]

        print(val[0][x],val[1][x],score)
    return score
