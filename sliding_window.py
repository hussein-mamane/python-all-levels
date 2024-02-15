my_list = list(range(1,10))
k = 3
#O(nk)
# for _ in range(0,len(my_list)-k+1):
#     new_list = my_list[_:_+k]
#     print(sum(new_list))

window_sum = sum(my_list[:k])  # Calculate the sum of the first k elements
print(window_sum)

for i in range(k, len(my_list)):
    window_sum = window_sum - my_list[i - k] + my_list[i]  # Update the sum by removing the first element and adding the next element
    print(window_sum)
