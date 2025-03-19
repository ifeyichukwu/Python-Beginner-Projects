#the list of words
list_of_odd_words = []
list_of_words = ["container", "flat", "crane", "from", "everyday", "taking", "over"]

#iterate over the words and find the odd ones
for word in list_of_words:
    if len(word) % 2 != 0:
        list_of_odd_words.append(word)

#print the list of odd numbers
print("This is the list of the odd numbered words: ", list_of_odd_words)