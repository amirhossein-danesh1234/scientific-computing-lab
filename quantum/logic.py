def is_num(a):
    try:
        float(a)
        return (True)
    except:
        return (False)


class im():
    def print_r(r):
        if (im.check(r)):
            a = r[0]
            b = r[1]
            print(f"{a} + i{b}")
        else:
            print("im print : it is not imagen number")


    def print_sin(r):
        if (im.check(r)):
            a = r[0]
            b = r[1]
            l = (a**2 + b**2) ** (0.5)
            tan_t = b/a
            cos_t = (1 / (tan_t**2) + 1) ** 0.5
            sin_t = 1 - (cos_t**2)
            print(f"r = {l} (({cos_t}) + i({sin_t}))")
        else:
            print("im print : it is not imagen number")


    def print_e(r):
        if (im.check(r)):
            a = r[0]
            b = r[1]
            print(f"{a} + i{b}")
        else:
            print("im print : it is not imagen number")

    def check(r):
        if (type(r) == list and len(r) == 2 and is_num(r[0]) and is_num(r[1])):
            return(True)
        else:
            return(False)
    


r = [3, 4]
im.print_sin(r)