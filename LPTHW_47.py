
def convert_number(s):
    try:
        print("this is your number", int(s))
    except ValueError:
        return "that's not a number"


convert_number("gg")