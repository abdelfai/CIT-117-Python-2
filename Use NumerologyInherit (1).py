from NumerologyLifePathDetails import NumerologyLifePathDetails #importing lifepathdetails
# getting name and dob
def main():
    name = input("Enter your full name: ")
    while not name:
        name = input("How do you not have a name? ")

    dob = input("Enter your Birthday (MM-DD-YYYY or MM/DD/YYYY): ")
    while not dob:
        dob = input("You were never born?")

    n = NumerologyLifePathDetails(name, dob)
#outputs
    print(f"Client name: {n.Name}")
    print(f"Client DOB: {n.Birthdate}")
    print(f"Life Path: {n.LifePath}")
    print(f"Life Path Description: {n.LifePathDescription}")
    print(f"Birthday: {n.BirthDay}")
    print(f"Attitude: {n.Attitude}")
    print(f"Soul: {n.Soul}")
    print(f"Personality: {n.Personality}")
    print(f"Power Name: {n.PowerName}")

if __name__ == "__main__":
    main()
