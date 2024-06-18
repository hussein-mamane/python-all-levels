import string
import regex

def drop_negatives(line,k):
    pass
def validate_input(line, k):
    if len(line.strip().split()) != k:
        raise ValueError("Use the correct declared number of values please")
    # drop negative
    #line_str = "".join(line.strip().split())
    drop_negatives(line,k)
    if not "".join(line.strip().split()).isdigit():
        raise ValueError("Use only digits please")


def compute_data(line:str, k: int) -> float:  # may be static -> out of any class
    # print(k, line, end="\n")
    try:
        validate_input(line,k)
    except ValueError as e:
        print("Non-Convertible, non-digit input was given: {}".format(e))
        exit(-1)
    return recursive_list_eval(list("".join(line.strip().split())))

def recursive_list_eval(line:list[str])->float:
    list_digit = line #.strip().split()
    if len(list_digit) == 1:
        return float(list_digit[0])**2
    return recursive_list_eval(list_digit[1:])+(float(list_digit[0]))**2 if float(list_digit[0]) > 0\
        else recursive_list_eval(list_digit[1:])




class Solution:
    number_of_lines_pair = 0

    # def __init__(self,nb_lines):
    #     self.number_of_lines_pair = nb_lines

    def read_compute_data(self):
        if self.number_of_lines_pair == 0:
            return 0.0
        k: int = int(input("Number of numbers: "))
        strs: str = input("Space-separated numbers: ")
        self.number_of_lines_pair -= 1 # class instance belongs to all instances
        return compute_data(strs,k) + self.read_compute_data()
    def __str__(self):
        return f'{self.number_of_lines_pair} is the number of lines'




if __name__ == '__main__':
    nb_lines: int  = int(input("number of operations"))
    print(nb_lines)
    s = Solution()
    s.number_of_lines_pair = nb_lines
    Solution.number_of_lines_pair = nb_lines
    print(s)
    print(Solution.number_of_lines_pair)
    print(s.read_compute_data())