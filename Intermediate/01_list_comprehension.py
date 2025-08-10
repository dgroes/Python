# Lista de compresión

# C017: List Comprehensions

my_original_list = ["Outer Wilds", "Fallout", "Bloodborne", "A Short Hike"]

my_list = [i for i in range(9)]
print(my_list)

my_list = [i * 2 for i in range(9)]
print(my_list)

my_list = [i * i for i in range(9)]
print(my_list)
my_list = [i * i for i in range(9)]
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(9)]
print(my_list)
