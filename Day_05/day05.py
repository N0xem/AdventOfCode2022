def day05_1():
    file = open("Day_05/input")
    crates = []
    crates2 = []
    y = 0
    step = 1
    for x in file:
        if step:
            crates.append([])
            for zeichen in range(len(x)):
                if zeichen % 4 == 1:
                    crates[y].append(x[zeichen])
            if len(crates[y]) == 0:
                crates = crates[:-2]
                step = 0
                for spalten in range(len(crates[0])):
                    crates2.append([])
                    for zeilen in range(len(crates)):
                        if crates[-zeilen-1][spalten]!=" ":
                            crates2[spalten].append(crates[-zeilen-1][spalten])
            y += 1
        else:
            command = x.split()
            print(command)
            for anzahl in range(int(command[1])):
                crates2[int(command[5])-1].append(crates2[int(command[3])-1][-1])
                crates2[int(command[3])-1].pop(-1)
                print(crates2)
    final = ""
    for x in range(len(crates2)):
        if len(crates2[x]) == 0:
            pass
        else:
            final += crates2[x][-1]
    return final

def day05_2():
    file = open("Day_05/input")
    crates = []
    crates2 = []
    y = 0
    step = 1
    for x in file:
        if step:
            crates.append([])
            for zeichen in range(len(x)):
                if zeichen % 4 == 1:
                    crates[y].append(x[zeichen])
            if len(crates[y]) == 0:
                crates = crates[:-2]
                step = 0
                for spalten in range(len(crates[0])):
                    crates2.append([])
                    for zeilen in range(len(crates)):
                        if crates[-zeilen-1][spalten]!=" ":
                            crates2[spalten].append(crates[-zeilen-1][spalten])
            y += 1
        else:
            command = x.split()
            print(command)
            for anzahl in range(int(command[1])):
                cranende = anzahl-int(command[1])
                crates2[int(command[5])-1].append(crates2[int(command[3])-1][cranende])
                crates2[int(command[3])-1].pop(cranende)
                print(crates2)
    final = ""
    for x in range(len(crates2)):
        if len(crates2[x]) == 0:
            pass
        else:
            final += crates2[x][-1]
    return final

