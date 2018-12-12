from pip._vendor.msgpack.fallback import xrange

f = open('./dist/2.txt', 'r').readlines()
stringsArr = [line.rstrip() for line in f]
previous = ''
position = 0
result = ''
string = []
for stringItemFirst in stringsArr:
    for j in range(1, len(stringsArr)):
        positions = [i for i in xrange(len(stringsArr[j])) if stringsArr[j][i] != stringItemFirst[i]]
        if len(positions) == 1:
            position = positions.pop()
            string = stringItemFirst

print(string[:position] + string[(position + 1):])