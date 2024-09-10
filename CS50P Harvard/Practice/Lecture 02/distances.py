distances = {
    "Voyager 1" : 163,
    "Voyager 2" : 136,
    "Pioneer 10" : 80,
    "New Horizons" : 58,
    "Pioneer 11" : 44
}

def main():
    print(keys(distances))
    print(values(distances))


def keys(distances):
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth.")

def values(distances):
    for distance in distances.values():
        print(f"{distance}AU in meters is {convert(distance)}m.")

def convert(au):
    return au * 149597870700
 
main()