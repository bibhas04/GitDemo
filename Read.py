file = open('test.txt')
# read all content of file
# Reading n number of characters by passing parameters
# print(file.read(5))
# Read one single line at a time
# print(file.readline())

# Print line by line using readline method:

# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()