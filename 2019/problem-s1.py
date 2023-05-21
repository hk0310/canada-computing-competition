countV = 0
countH = 0

listV1 = [1, 2]
listV2 = [3, 4]
listH = [listV1, listV2]

y = input()

y = y.lower()
y = y.lower()
for c in y:
    if c == "v":
        countV += 1
    elif c == "h":
        countH += 1
if countV % 2 == 1:
    listV1 = listV1.reverse()
    listV2 = listV2.reverse()

if countH % 2 == 1:
    listH == listH.reverse()

for l in listH:
        print(*l, sep= " ")

