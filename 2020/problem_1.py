observations = {}
speed = []
rep = input()

for i in range(int(rep)):
    timepos = input()
    observations[int(timepos[: timepos.find(" ")])] = int(timepos[timepos.find(" ") + 1:])

keybefore = None
for key in sorted(observations.keys()):
    if keybefore == None:
        keybefore = key
    elif keybefore != key:
        speedi =(observations[key] - observations[keybefore]) / (key - keybefore)
        if speedi < 0:
            speedi = speedi * -1
        speed.append(speedi)
        keybefore = key

speed.sort()
print (speed[-1])















