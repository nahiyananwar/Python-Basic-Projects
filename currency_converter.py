'''
Write a program to convert an amount of money from one currency to another
using fixed exchange rates. The user inputs the amount and selects the currencies
for conversion.

-> Modify the program so that the user can see the equivalent amount in several
different currencies at the same time. For example, converting 100 USD to
EUR, CAD, and GBP all at once.

-> Expand the list of available currencies for conversion. This might involve
adding more fixed exchange rates to the program.

-> Keep a history of the most recent conversions made during the session and
display this history at the end of the program.

'''


def currency_converter(amount, src, target):

    euro_to_cad = 1.6269124
    cad_to_euro = 0.61466126
    euro_to_gbp = 0.87256537
    gbp_to_euro = 1.1460459
    cad_to_gbp = 0.53633982
    gbp_to_cad = 1.8646813

    if src == "EUR" and target == "CAD":
        rate = euro_to_cad * amount
        print(f"\n{amount} Euro is equal to {rate} Cad.")

    elif src == "CAD" and target == "EUR":
        rate = cad_to_euro * amount
        print(f"\n{amount} Cad is equal to {rate} Euro.")

    elif src == "EUR" and target == "GBP":
        rate = euro_to_gbp * amount
        print(f"\n{amount} Euro is equal to {rate} British Pound.")

    elif src == "GBP" and target == "EUR":
        rate = gbp_to_euro * amount
        print(f"\n{amount} Pound sterling is equal to {rate} Euro.")

    elif src == "CAD" and target == "GBP":
        rate = cad_to_gbp * amount
        print(f"\n{amount} Cad is equal to {rate} British Pound.")

    elif src == "GBP" and target == "CAD":
        rate = gbp_to_cad * amount
        print(f"\n{amount} Pound sterling is equal to {rate} Cad.")

    elif src == target:
        print(f"{amount} {src} is equal to {amount} {target}.")


def amount_validation(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            print("\nAmount must be greater than 0.")
            return None
        else:
            return amount

    except ValueError:
        print("\nEnter a valid number.")
        return None


def main():
    amount = input("\nEnter the amount you want to convert:\n> ")
    val_amount = amount_validation(amount)

    src = input("\nSource currency (EUR/CAD/GBP): ").upper()
    target = input("\nTarget currency (EUR/CAD/GBP): ").upper()

    if src not in ["EUR", "CAD", "GBP"] or target not in ["EUR", "CAD", "GBP"]:
        print("\nEnter either EUR, CAD or GBP.")
        return

    currency_converter(val_amount, src, target)


main()
