def main():
    tweet = input("Tweet: ")
    print(shorten(tweet))

def shorten(word):
    vowel = ["a", "e", "i", "o", "u"]
    twt = ""
    for letter in word:
        if letter.lower() not in vowel:
            twt += letter
    return twt


if __name__ == "__main__":
    main()


"""
def main():
    tweet = input("Tweet: ")
    twt = shorten(tweet)
    print("Output: ", twt)

def shorten(word):
    vowel = ["a", "e", "i", "o", "u"]
    twt = []
    for letter in word:
        if letter not in vowel:
            twt.append(letter)
    twt_str = str("".join(twt))
    return twt_str

if __name__ == "__main__":
    main()
"""