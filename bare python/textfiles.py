file = open("text.txt", 'r', encoding="utf-8", newline="")
can_read_file = file.readable()


print('Testing readline and readlines')
if can_read_file:
    data = file.readline()  # readlines len = 3 ['Mario on the first line\n', 'Sonic on the second line\n', 'The third line is slow']
    print(len(data))
    print(data)  # readline 'Mario on the first line\n' len = 24, \n is counted

#
# print('Testing read')
# if can_read_file:
#     print(file.read()) # emptying the file, nothing is left in now
#     print(file.read())
file.close()

with open('text_write.txt', 'w', encoding="utf-8", newline="") as f:
    f.write("HelloWriter")