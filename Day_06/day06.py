def day06_1():
    file = open("Day_06/input")
    code = 4
    for x in file:
        for zeichen in range(len(x)):
            vergleich = []
            for y in range(code):
                vergleich.append(ord(x[zeichen + y]))
            vergleich.sort()
            zahl = 1
            for z in range(code - 1):
                zahl *= vergleich[z] - vergleich[z + 1]
                print(vergleich)

            if zahl != 0:
                return zeichen + code

def day06_2():
    file = open("Day_06/input")
    code = 14
    for x in file:
        for zeichen in range(len(x)):
            vergleich = []
            for y in range(code):
                vergleich.append(ord(x[zeichen+y]))
            vergleich.sort()
            zahl = 1
            for z in range(code-1):
                zahl *= vergleich[z]-vergleich[z+1]
                print(vergleich)

            if zahl != 0:
                return zeichen + code