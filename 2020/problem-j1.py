#! python3

score = 0
for i in range(3):
    u = int(input())
    if i == 0:
        score = score + (u*1)
    if i == 1:
        score = score + (u*2)
    if i == 2:
        score += (u*3)
if score >= 10:
    print("happy")
else:
    print("sad")
