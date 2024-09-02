def main():
    msg = input()
    print(convert(msg))

def convert(m):
    m1 = m.replace(":)","🙂")
    m2 = m1.replace(":(","🙁")
    return m2


main()
