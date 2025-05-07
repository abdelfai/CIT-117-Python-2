class Numerology:
    def __init__(self, sName, sDOB):
        self.name = sName.upper() # upper for consistency
        self.dob = sDOB.replace("/", "-")
        self.VOWEL_SET = set("AEIOU") #setting the vowels
#returning name
    def getName(self):
        return self.name
#returning bday
    def getBirthdate(self):
        return self.dob

    def getLifePath(self):
        digits = [int(ch) for ch in self.dob if ch.isdigit()]
        total = sum(digits)
        return self.number_reduce(total)
# getting the day from bday
    def getBirthDay(self):
        day = int(self.dob.split("-")[1])
        return self.number_reduce(day) #single digits only!!!!!!

    def getAttitude(self):
        parts = self.dob.split("-")
        month = sum(int(ch) for ch in parts[0]) #the month
        day = sum(int(ch) for ch in parts[1]) #the day
        return self.number_reduce(month + day) # single digits!

    def getSoul(self):
        total = sum(self.NUMBER_MAP(ch) for ch in self.name if ch in self.VOWEL_SET)
        return self.number_reduce(total) #single digit, why cant the digits ever find love?

    def getPersonality(self):
        total = sum(self.NUMBER_MAP(ch) for ch in self.name if ch.isalpha() and ch not in self.VOWEL_SET) #adding the vowels in birth name
        return self.number_reduce(total) #poor digits
#calculating power from soul and personality
    def getPowerName(self):
        return self.number_reduce(self.getSoul() + self.getPersonality())

#mapping the numbers
    def NUMBER_MAP(self, ch):
        mapping = {
            "A": 1, "J": 1, "S": 1,
            "B": 2, "K": 2, "T": 2,
            "C": 3, "L": 3, "U": 3,
            "D": 4, "M": 4, "V": 4,
            "E": 5, "N": 5, "W": 5,
            "F": 6, "O": 6, "X": 6,
            "G": 7, "P": 7, "Y": 7,
            "H": 8, "Q": 8, "Z": 8,
            "I": 9, "R": 9
        }
        return mapping.get(ch, 0)
# reducing number to only single digits
    def number_reduce(self, num):
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num
#outputs
    def __str__(self):
        return (
            f"Client name:{self.name}\n"
            f"Client DOB:{self.dob}\n"
            f"Life Path:{self.getLifePath()}\n"
            f"Attitude:{self.getAttitude()}\n"
            f"Birthday:{self.getBirthDay()}\n"
            f"Personality:{self.getPersonality()}\n"
            f"Power Name:{self.getPowerName()}\n"
            f"Soul:{self.getSoul()}\n"
            
        )
#fun code, only took me a week to understand. 
