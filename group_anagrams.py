input_initial = ["abv", "afd", "fda", "del", "vba", "led", "eld"]

"""
# what is the complexity
def anagram_grouper(input_list: list[str]) -> list[list[str]]:
    def get_group_num(input_str: str) -> int:
        i:int = 0
        for lst in result:
            if lst is not None and sorted(input_str) == sorted(lst[0]):
                return i
            i+=1
        return -1
    #list of lists
    result = []

    for input_str in input_list:
        group_num = get_group_num(input_str)
        if group_num != -1:
            result[group_num].append(input_str)
        else:
            result.append([input_str])
    return result
print("finally",anagram_grouper(input_initial))
"""

