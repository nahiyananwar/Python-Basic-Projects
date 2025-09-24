'''
print the user input numbers in alphabets. e.g.,(1 -> One, 11 -> Eleven)

'''


def get_user_input():
    while True:
        user_input = input("\nEnter numbers separated by a comma(,):\n> ")
        user_input = user_input.split(",")

        numbers = []
        invalid = False
        for user in user_input:
            user = user.strip()
            if user.isdigit():
                numbers.append(int(user))

            else:
                invalid = True

        if invalid:
            print("\nInvalid Input. Enter numbers only.")
        else:
            return numbers


def number_calling():

    user_input = get_user_input()

    grt_10 = "teen"
    grt_20 = "twenty"
    grt_30 = "thirty"
    grt_40 = "fourty"
    grt_50 = "fifty"
    grt_60 = "sixty"
    grt_70 = "seventy"
    grt_80 = "eighty"
    grt_90 = "ninety"

    number_mapping_one_to_ten = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        0: "Zero"
    }
    number_mapping_11_to_19 = {
        11: "Eleven",
        12: "Twelve",
        13: "Thir"+grt_10,
        14: number_mapping_one_to_ten.get(4)+grt_10,
        15: "Fif"+grt_10,
        16: number_mapping_one_to_ten.get(6) + grt_10,
        17: number_mapping_one_to_ten.get(7)+grt_10,
        18: "Eigh"+grt_10,
        19: number_mapping_one_to_ten.get(9)+grt_10
    }
    number_mapping_20_to_29 = {
        20: grt_20,
        21: (grt_20 + number_mapping_one_to_ten.get(1)),
        22: (grt_20 + number_mapping_one_to_ten.get(2)),
        23: (grt_20 + number_mapping_one_to_ten.get(3)),
        24: (grt_20 + number_mapping_one_to_ten.get(4)),
        25: (grt_20 + number_mapping_one_to_ten.get(5)),
        26: (grt_20 + number_mapping_one_to_ten.get(6)),
        27: (grt_20 + number_mapping_one_to_ten.get(7)),
        28: (grt_20 + number_mapping_one_to_ten.get(8)),
        29: (grt_20 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_30_to_39 = {
        30: grt_30,
        31: (grt_30 + number_mapping_one_to_ten.get(1)),
        32: (grt_30 + number_mapping_one_to_ten.get(2)),
        33: (grt_30 + number_mapping_one_to_ten.get(3)),
        34: (grt_30 + number_mapping_one_to_ten.get(4)),
        35: (grt_30 + number_mapping_one_to_ten.get(5)),
        36: (grt_30 + number_mapping_one_to_ten.get(6)),
        37: (grt_30 + number_mapping_one_to_ten.get(7)),
        38: (grt_30 + number_mapping_one_to_ten.get(8)),
        39: (grt_30 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_40_to_49 = {
        40: grt_40,
        41: (grt_40 + number_mapping_one_to_ten.get(1)),
        42: (grt_40 + number_mapping_one_to_ten.get(2)),
        43: (grt_40 + number_mapping_one_to_ten.get(3)),
        44: (grt_40 + number_mapping_one_to_ten.get(4)),
        45: (grt_40 + number_mapping_one_to_ten.get(5)),
        46: (grt_40 + number_mapping_one_to_ten.get(6)),
        47: (grt_40 + number_mapping_one_to_ten.get(7)),
        48: (grt_40 + number_mapping_one_to_ten.get(8)),
        49: (grt_40 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_50_to_59 = {
        50: grt_50,
        51: (grt_50 + number_mapping_one_to_ten.get(1)),
        52: (grt_50 + number_mapping_one_to_ten.get(2)),
        53: (grt_50 + number_mapping_one_to_ten.get(3)),
        54: (grt_50 + number_mapping_one_to_ten.get(4)),
        55: (grt_50 + number_mapping_one_to_ten.get(5)),
        56: (grt_50 + number_mapping_one_to_ten.get(6)),
        57: (grt_50 + number_mapping_one_to_ten.get(7)),
        58: (grt_50 + number_mapping_one_to_ten.get(8)),
        59: (grt_50 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_60_to_69 = {
        60: grt_60,
        61: (grt_60 + number_mapping_one_to_ten.get(1)),
        62: (grt_60 + number_mapping_one_to_ten.get(2)),
        63: (grt_60 + number_mapping_one_to_ten.get(3)),
        64: (grt_60 + number_mapping_one_to_ten.get(4)),
        65: (grt_60 + number_mapping_one_to_ten.get(5)),
        66: (grt_60 + number_mapping_one_to_ten.get(6)),
        67: (grt_60 + number_mapping_one_to_ten.get(7)),
        68: (grt_60 + number_mapping_one_to_ten.get(8)),
        69: (grt_60 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_70_to_79 = {
        70: grt_70,
        71: (grt_70 + number_mapping_one_to_ten.get(1)),
        72: (grt_70 + number_mapping_one_to_ten.get(2)),
        73: (grt_70 + number_mapping_one_to_ten.get(3)),
        74: (grt_70 + number_mapping_one_to_ten.get(4)),
        75: (grt_70 + number_mapping_one_to_ten.get(5)),
        76: (grt_70 + number_mapping_one_to_ten.get(6)),
        77: (grt_70 + number_mapping_one_to_ten.get(7)),
        78: (grt_70 + number_mapping_one_to_ten.get(8)),
        79: (grt_70 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_80_to_89 = {
        80: grt_80,
        81: (grt_80 + number_mapping_one_to_ten.get(1)),
        82: (grt_80 + number_mapping_one_to_ten.get(2)),
        83: (grt_80 + number_mapping_one_to_ten.get(3)),
        84: (grt_80 + number_mapping_one_to_ten.get(4)),
        85: (grt_80 + number_mapping_one_to_ten.get(5)),
        86: (grt_80 + number_mapping_one_to_ten.get(6)),
        87: (grt_80 + number_mapping_one_to_ten.get(7)),
        88: (grt_80 + number_mapping_one_to_ten.get(8)),
        89: (grt_80 + number_mapping_one_to_ten.get(9)),
    }
    number_mapping_90_to_99 = {
        90: grt_90,
        91: (grt_90 + number_mapping_one_to_ten.get(1)),
        92: (grt_90 + number_mapping_one_to_ten.get(2)),
        93: (grt_90 + number_mapping_one_to_ten.get(3)),
        94: (grt_90 + number_mapping_one_to_ten.get(4)),
        95: (grt_90 + number_mapping_one_to_ten.get(5)),
        96: (grt_90 + number_mapping_one_to_ten.get(6)),
        97: (grt_90 + number_mapping_one_to_ten.get(7)),
        98: (grt_90 + number_mapping_one_to_ten.get(8)),
        99: (grt_90 + number_mapping_one_to_ten.get(9)),
    }

    output = ""
    for user in user_input:
        if user <= 10:
            output += number_mapping_one_to_ten.get(user, "!") + " "
        elif 11 <= user < 20:
            output += number_mapping_11_to_19.get(user, "!") + " "
        elif 20 <= user < 30:
            output += number_mapping_20_to_29.get(user, "!") + " "
        elif 30 <= user < 40:
            output += number_mapping_30_to_39.get(user, "!") + " "
        elif 40 <= user < 50:
            output += number_mapping_40_to_49.get(user, "!") + " "
        elif 50 <= user < 60:
            output += number_mapping_50_to_59.get(user, "!") + " "
        elif 60 <= user < 70:
            output += number_mapping_60_to_69.get(user, "!") + " "
        elif 70 <= user < 80:
            output += number_mapping_70_to_79.get(user, "!") + " "
        elif 80 <= user < 90:
            output += number_mapping_80_to_89.get(user, "!") + " "
        elif 20 <= user < 100:
            output += number_mapping_90_to_99.get(user, "!") + " "

    print(output)


number_calling()
