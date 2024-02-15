from collections import Counter
moves = "UULDRD"
def robot_return_to_origin(moves:list[int])->bool:
    counts = Counter(moves)
    return (counts['U'] == counts['D'])\
        and (counts['L'] == counts['R'])

print(robot_return_to_origin(moves))