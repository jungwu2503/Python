infile = open("sample.txt", "r")
#infile = open("c:\Temp\myMath.py", "r")

data = infile.readlines()

#while data != "":
    #print(data, end='')
#    print(data.rstrip())
#    data = infile.readline()

for line in data:
    print(line.rstrip())

#print(data)
infile.close()

print(type(data))
print(type(infile))

