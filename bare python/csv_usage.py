import csv

f = open('data.csv', 'r')


reader = csv.reader(f)

data = list(reader)
# header = next(reader)

print(reader)
print(data)
print(data[0][0])
# print(header)

f.close()
