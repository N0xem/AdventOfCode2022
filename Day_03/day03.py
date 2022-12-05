def compare(wert):
    for rucksack_a in wert[0]:
        for rucksack_b in wert[1]:
            if ord(rucksack_a) == ord(rucksack_b):
                if ord(rucksack_a) < 96:
                    return ord(rucksack_a) - 64 + 26
                else:
                    return ord(rucksack_a) - 96
    return 0


def day03_1():
    file = open("Day_03/input")
    summe = 0

    for x in file:
        wert = [x[:int(len(x)/2)], x[int(len(x)/2):]]
        summe += compare(wert)
    return(summe)

def day03_2():
    file = open("Day_03/input")
    summe = 0
    presumme = 0
    subgroup = []

    for x in file:
        subgroup.append(x.split("\n")[0])
    for com1 in range(len(subgroup)):
        presumme = summe
        for com2 in range(com1+1, len(subgroup)-1):
            if compare([subgroup[com1], subgroup[com2]]) > 0:
                for com3 in range(com2+1, len(subgroup)-1):
                    print(subgroup[com1], subgroup[com2], subgroup[com3],compare([subgroup[com1]+subgroup[com2], subgroup[com3]]))
                    summe += compare([subgroup[com1]+subgroup[com2], subgroup[com3]])
                if presumme == summe:
                    print(com1)

    return(summe)

