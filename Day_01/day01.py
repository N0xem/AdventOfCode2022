
def day01_1():
    file = open("Day_01/input")

    max_wert = 0
    summe = 0

    for x in file:
        if x =="\n":
            if summe > max_wert:
                max_wert = summe
            summe = 0
        else:
            summe += int(x[:-1])
    return max_wert

def day01_2():

    file = open("Day_01/input")
    summen = []
    summe=0

    for x in file:
        print(x)
        if x == "\n":
            summen.append(summe)

            summe = 0
        else:
            summe += int(x[:-1])
    summen.sort()

    max_wert = summen[-1]+summen[-2]+summen[-3]
    return max_wert