# A simple program to convert currency

print("Hi there, welcome this is a simple currency convertor")
amount = float(input("Enter the amount you want to convert: "))

curr_currency = input("""Choose the current currency from below:\n"""
                      """1.USD.\n"""
                      """2.EUR.\n"""
                      """3.GBP.\n"""
                      """4.TZS.\n"""
                      """5.UGX.\n"""
                      """6.JPY.\n"""
                      """7.KSH.\n""").lower()

to_currency = input("""Choose the currency you want to convert to from below:\n"""
                      """1.USD.\n"""
                      """2.EUR.\n"""
                      """3.GBP.\n"""
                      """4.TZS.\n"""
                      """5.UGX.\n"""
                      """6.JPY.\n"""
                      """7.KSH.\n""").lower()

if curr_currency == to_currency:
    print("Error you cant convert same currency")
    exit()
def convert(amount, curr_currency, to_currency):
    if curr_currency == "1":
        converted_currency = amount * 1.0
    elif curr_currency == "2":
        converted_currency = amount * 141.75
    elif curr_currency == "3":
        converted_currency = amount * 165.32
    elif curr_currency == "4":
        converted_currency = amount * 0.0673
    elif curr_currency == "5":
        converted_currency = amount * 0.0528
    elif curr_currency == "6":
        converted_currency = amount * 93.04
    elif curr_currency == "7":
        converted_currency = amount * 133.5
    else:        
        return "Invalid current currency"
    return converted_currency

print(convert(amount, curr_currency, to_currency))