heroes = ["spider_man", "skywalker", "fisher", "wolverine","indiana_jones"]
universes = ["mcu", "star_wars", "ubisoft", "mcu"]

for h, u in zip(heroes, universes):
    print(h, u)

# dict comprehension
squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(squares)

# one element list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
print([n-1 for n in numbers]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# two element list comprehension
numbers2 = [11,12,13,14,15,16,17,18,19]

sum_numbers = [a+b for a in numbers2 for b in numbers2]
print(sum_numbers)
print('length = ', len(sum_numbers))