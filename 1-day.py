f = open('dist/1.txt', 'r').readlines()
numbers = [int(line.rstrip()) for line in f]
print(sum(numbers))