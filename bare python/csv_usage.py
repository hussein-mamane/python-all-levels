import csv

f = open('data.csv', 'r')


reader = csv.reader(f)

data = list(reader)
# header = next(reader)

print(reader) # _csv.reader object
print(data)
print(data[0][0])
# print(header)

f.close()
