tweet = input("Tweet: ")
print("twt: ", end="")

vowel = ["a", "e", "i", "o", "u"]

for letter in tweet:
    if letter not in vowel:
        print(letter,end="")
