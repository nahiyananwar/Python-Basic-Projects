'''
create a program that will convert symbols into emojis. e.g., I am sad :( -> I am sad 😞.

'''


def emojis():
    emoji = {
        ":)": '😊',
        ":(": '😞'
    }
    return emoji


def user_input():
    text = input("\nEnter a text:\n> ")

    return text


def emoji_converter():
    text = user_input()
    text = text.split(" ")
    emoji = emojis()

    output = ""
    for t in text:
        output += emoji.get(t, t) + " "

    print(output)


emoji_converter()
