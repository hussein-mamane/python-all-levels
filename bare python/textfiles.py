file = open("text.txt", 'r', encoding="utf-8", newline="")
can_read_file = file.readable()
if can_read_file:
    data = file.readline()
    print(len(data))
