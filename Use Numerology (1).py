from Numerology import Numerology #impoerting numerology

def main():
    name = input("Enter your full name: ")
    while not name:
        name = input("how do you not have a name?")

    dob = input("Enter your Birthday (MM-DD-YYYY or MM/DD/YYYY): ")
    while not dob:
        dob = input("You were never born?")

    numerology = Numerology(name, dob)
    print("\n" + str(numerology))

if __name__ == "__main__":
    main()
