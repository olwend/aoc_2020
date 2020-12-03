import io, itertools

numbers = open("aoc.txt")
numbers_list = [int(line.replace('\n',''))for line in numbers.readlines()]
print(sorted(numbers_list))
all_expense_pairs = list(itertools.combinations(numbers_list, 2))
# print(all_expense_pairs)
print(len(all_expense_pairs))

def sums_to_2020(values):
    return sum(values) == 2020
result = list(filter(sums_to_2020, all_expense_pairs))
print(result)

# manual step to  calculate 1018 * 1002 = 1020036

# Part 2 - product of 3 entries that sum to 2020
all_expense_trebles = list(itertools.combinations(numbers_list, 3))
print(len(all_expense_trebles))
result_trebles = list(filter(sums_to_2020, all_expense_trebles))
print(result_trebles)

# manual step to  calculate 522 * 855 * 643 = 286977330
# 
# learning python credit to https://www.globalnerdy.com/