import re
from collections import defaultdict
from dateutil import parser

WAKES_UP = 'wakes up'
FALLS_ASLEEP = 'falls asleep'
f = open('../../dist/4.txt', 'r').readlines()
linesArr = [line.rstrip() for line in f]
dictionary = sorted({re.search('\[(.*)]', item).group(1): item.split(']')[1][1:] for item in linesArr}.items())
guardID = 0
infoByGuards = defaultdict(list)
for date, value in dictionary:
    if value != WAKES_UP and value != FALLS_ASLEEP:
        guardID = ''.join(c for c in value if c.isdigit())
    elif value == FALLS_ASLEEP:
        infoByGuards[guardID].append({'sleepTime': date})
    else:
        infoByGuards[guardID].append({'wakesTime': date})
countingByGuards = defaultdict(list)
for guardID, values in infoByGuards.items():
    startSleep = ''
    endSleep = ''
    minutes = 0
    minutesSum = 0
    maxMin = 0
    for action in values:
        parsed = [item for item in action.items()].pop()
        actionName = parsed[0]
        date = parsed[1]
        if  actionName == 'sleepTime':
            startSleep = parser.parse(date)
        else:
            minutes = int((parser.parse(date) - startSleep).seconds / 60)
        minutesSum += minutes
        if maxMin < minutes:
            maxMin = minutes
    countingByGuards[guardID].append([minutesSum, maxMin])

maxGuardId = 0
maxSleep = 0
for guardID, data in countingByGuards.items():
    if maxSleep < data[0][0]:
        maxGuardId = guardID
maxTimeResult = countingByGuards[maxGuardId].pop()[1]
print(int(maxGuardId))
print(int(maxGuardId) * int(maxTimeResult) - 1)

