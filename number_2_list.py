#Read a file with a number in each line and output a list
#Please run it in terminal

from sys import argv
script, file_name = argv

f = open(file_name)
result = []

for line in f.readlines():
       result.append(int(line))

print result
