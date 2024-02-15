initial_array = [2, 11, 7, 15]
target = 9
# solution in O()
# first quick sort the elements in dual pivot quick sort O(nlogn)
# then use two pointers start and end and move the one that
# approach you to the result


# evident solution in O(n2)
# stop = False
# k = t = 0
# for i in initial_array:
#     for j in initial_array:
#         if i + j == target:
#             print(i, j)
#             stop = True
#             break
#         t += 1
#     if stop:
#         break
#     k += 1
#     t = 0
# print(k,t)
