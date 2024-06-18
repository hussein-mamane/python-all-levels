# def recursive_clean(lst, n):
#     if n == 0:
#         return lst
#     if lst[0] == '-':
#         if n == 2:
#             return []
#         if n == 3:
#             return list(lst[-1])
#         return recursive_clean(lst[2:], n - 2)
#     else:
#         lst.append(lst[0])
#         return recursive_clean(lst[1:], n - 1)
#
#
# print(recursive_clean(['-', '1', '2', '-', '3'], 5))
def clean_negatives(lst):
    if not lst:
        return []

    # If the first element is a negative signs
    if lst[0] == '-':
        print("From 2 ---", lst[2:])
        # Skip the next element as well and recursively call the function on the rest of the list
        return clean_negatives(lst[2:])
    else:
        # Keep the current element and recursively process the rest of the list
        print("From 1 ---",lst[1:])
        return [lst[0]] + clean_negatives(lst[1:])


# Example usage
original_list = ['-', '1', '2', '-', '3']
cleaned_list = clean_negatives(original_list)
print(cleaned_list)  # Output: ['2']