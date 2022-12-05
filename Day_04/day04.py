def day04_1():
    file = open("Day_04/input")
    summe = 0

    for x in file:
        scope = x.split("\n")[0].split(",")
        scope = [scope[1].split("-"), scope[0].split("-")]
        scope =[int(scope[0][0]),int(scope[0][1]),int(scope[1][0]),int(scope[1][1])]
        if scope[0] <= scope[2] and scope[1] >= scope[3] or scope[2] <= scope[0] and scope[3] >= scope[1]:
                summe += 1
    return summe
def day04_2():
    file = open("Day_04/input")
    summe = 0

    for x in file:
        scope = x.split("\n")[0].split(",")
        scope = [scope[0].split("-"), scope[1].split("-")]
        scope = [int(scope[0][0]), int(scope[0][1]), int(scope[1][0]), int(scope[1][1])]
        print(scope)
        if max(scope[0], scope[2]) <= min(scope[1], scope[3]):
            print(summe, scope)
            summe += 1
    return summe


