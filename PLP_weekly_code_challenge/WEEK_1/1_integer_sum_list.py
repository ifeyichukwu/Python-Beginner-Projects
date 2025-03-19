# a = int(input("Please enter your first number: "))
# b = int(input("Please enter your second number: "))
# c = int(input("Please enter your third number: "))
# d = int(input("Please enter your fourth number: "))
# e = int(input("Please enter your fifth number: "))

# integers = [a, b, c, d, e]  # Store numbers in a list

# total = sum(integers)  # Calculate the sum

# print("The sum of the numbers is:", total)

try: 
    numbers = list(map(int, input("Enters numbers separated by spaces: ").split()))
    total = sum(numbers) #compute sum
    print("The sum of the numbers is:", total)

except ValueError:
    print("Invalid input! Please enter only numbers.")
