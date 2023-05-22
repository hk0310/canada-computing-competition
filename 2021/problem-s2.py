row_number = int(input())
collumn_number = int(input())

choose = []

canvas = [["B" for z in range(collumn_number)] for y in range(row_number)]

choice_number = int(input())
for i in range(choice_number):
    choice = input()
    choose = choice.split()

    if choose[0] == "R":
        for a in range(collumn_number):
            if canvas[int(choose[1]) - 1][a] == "B":
                canvas[int(choose[1]) - 1][a] = "G"
            elif canvas[int(choose[1]) - 1][a] == "G":
                canvas[int(choose[1]) - 1][a] = "B"
    elif choose[0] == "C":
        for b in range(row_number):
            if canvas[b][int(choose[1]) - 1] == "B":
                canvas[b][int(choose[1]) - 1] = "G"
            elif canvas[b][int(choose[1]) - 1] == "G":
                canvas[b][int(choose[1]) - 1] = "B"

count = 0
for d in range(row_number):
    for e in range(collumn_number):
        if canvas[d][e] == "G":
            count += 1

print(count)
