initial_array = ['a', 'n', 'b', 'c']
initial_array_2 = ['a', 'n', 'b', 'c', 'b', 'c', 'c']


def duplicate_checker(lst: list) -> bool:
    the_set = set()
    for an_element in lst:
        if an_element in the_set:
            return True
        else:
            the_set.add(an_element)
    return False


print(duplicate_checker(initial_array))
print(duplicate_checker(initial_array_2))
