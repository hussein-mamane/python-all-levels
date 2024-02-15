import itertools
l: int = 2
initial_array = ['a', 'n', 'b', 'c', 'b', 'c', 'c']
counting_map = dict()
for i in initial_array:
    if i in counting_map.keys():
        counting_map[i] += 1
    else:
        counting_map[i] = 1
print("Here is the counting map")
print(counting_map.items())
print(type(counting_map.items()))
ordered_map = {k: v for k, v in sorted(counting_map.items(),
                                       key=lambda item: item[1], reverse=True)}
# print(counting_map.__contains__('r'))
# taking l first elements
final_result = dict(itertools.islice(ordered_map.items(),l))
print(final_result.values())