
"""
Gio's code
import random


def main():
    level = get_level()
    score = simulate_game(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x,y

def simulate_round(x,y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f" {x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                count_tries =+ 1
                print("EEE")
        except:
            count_tries =+ 1
            print("EEE")
    print(f'{x} + {y} = {x+y}')
    return False


def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()
"""

#My code
import random


def main():
    #call get_level()
    level = get_level()
    #get the score
    score = 0
    problems_generated = 0
    while problems_generated < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempts = 0
        while attempts < 3:
            try:
                user_answer = int(input(f' {x} + {y} ='))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    attempts += 1
                    print("EEE")
            except ValueError:
                print("EEE")
                attempts += 1
        if attempts == 3:
            print(f"Correct answer: {answer}")
            break
        problems_generated += 1
    print(f"Your score: {score}/10")
    #print


def get_level():
    #loop forever
    #prompts( and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
    while True:
        try:
            level = int(input("Level (1,2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Level needs to be either 1, 2, or 3.")
                pass
        except ValueError:
            print("Invalid level. Please enter 1, 2, or 3.")
            pass


def generate_integer(level):
    #returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()