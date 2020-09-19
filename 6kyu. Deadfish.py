def parse(data):
    num = 0
    result = []
    data = data.lower()
    for letter in data:
        if letter != "i" and letter != "d" and letter != "s" and letter != "o":
            pass
        if letter == "i":
            num += 1
        if letter == "d":
            num -= 1
        if letter == "s":
            num *= num
        if letter == "o":
            result.append(num)
    return result




#i increments the value (initially 0)
#d decrements the value
#s squares the value
#o outputs the value into the return array
parse("iiisdoso")
