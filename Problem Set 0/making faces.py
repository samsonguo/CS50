def main():
    user_input = input("Input: ")
    final_user_input = convert(user_input)
    print(final_user_input)

def convert(user_input):
    user_input = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return user_input

main()