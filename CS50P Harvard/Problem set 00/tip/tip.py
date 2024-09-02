def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dd = d.replace("$","")
    dd1 = float(dd)
    return dd1

def percent_to_float(p):
    pp = p.replace("%","")
    pp1 = int(pp)
    pp2 = pp1/100
    return pp2


main()
