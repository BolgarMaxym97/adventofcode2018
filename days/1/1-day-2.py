f = open('./dist/1.txt', 'r').readlines()
numbers = [int(line.rstrip()) for line in f]
sumByStep = []
current = 0
result = 0
while result == 0:
    for numberItem in numbers:
        current += numberItem
        sumByStep.append(current)
        if sumByStep.count(current) == 2:
            result = current
            break
print(result)