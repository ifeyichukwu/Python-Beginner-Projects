name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
favourite_color = input("What is your favourite color: ")

personal_information = {
    "Name": name,
    "Age": age,
    "Favourite color": favourite_color,
}

#print the information in a more readable format
print("\n📌 This is the user's personal information: ")
for key, value in personal_information.items():
    print(f"{key}: {value}")