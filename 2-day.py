f = open('dist/2.txt', 'r').readlines()
stringsArr = [line.rstrip() for line in f]
threeCount = 0
twoCount = 0

for stringItem in stringsArr:
    my_list = list(stringItem)
    get_unique_char = set(my_list)
    twoCheck = False
    threeCheck = False
    for key in get_unique_char:
        if stringItem.count(key) == 3 and not threeCheck:
            threeCount += 1
            threeCheck = True
            continue
        if stringItem.count(key) == 2 and not twoCheck:
            twoCount += 1
            twoCheck = True
            continue
    continue
print(threeCount * twoCount)
