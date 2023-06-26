def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = float(d.replace('$',''))
    #print(f"{d:.1f}")
    return d

def percent_to_float(p):
    # TODO
    p = float(p.replace('%',''))
    p = p/100.0
    return p

main()