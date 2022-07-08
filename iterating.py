def standart():
    with open("list.csv") as file:
        for line in file:
            print(line.upper())

def another():
    file = open("list.csv")
    lines = file.readlines()
    file.close()
    lines.sort()
    print(lines)

standart()
another()