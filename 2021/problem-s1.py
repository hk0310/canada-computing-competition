piece = int(input())
side = []
width = []
area = []

sides = input()
side = sides.split()

widths = input()
width = widths.split()

for i in range(piece):
    areas = (int(side[i]) + int(side[i + 1])) * int(width[i]) / 2
    area.append(areas)
total_area = 0
for i in range(len(area)):
    total_area += area[i]

print(total_area)
