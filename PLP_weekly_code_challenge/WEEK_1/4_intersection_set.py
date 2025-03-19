#accepting the input of two sets
set_1 = set(map(int, input("Put in your integer values for the first set by separating with spaces: ").split()))
set_2 = set(map(int, input("Put in your integer values by separating with spaces: ").split()))

#finding the numbers that are in both sets
common_elements = set_1 & set_2

#printing the numbers which are in the two sets
print("Common Elements: ", ", ".join(map(str, common_elements)))
