class Numerology:
    def __init__(self, sName, sDOB): 
        self.__name = sName.upper()
        self.__dob = sDOB.replace("/", "-")
        self.VOWEL_SET = set("AEIOU")
#all calculations from previous assignment
        digits = [int(ch) for ch in self.__dob if ch.isdigit()]
        parts = self.__dob.split("-")

        self.__iLifePathNumber = self.__reduceNumber(sum(digits))
        self.__iBirthdayNumber = self.__reduceNumber(int(parts[1]))
        self.__iAttitudeNumber = self.__reduceNumber(
            sum(int(ch) for ch in parts[0]) + sum(int(ch) for ch in parts[1])
        )
        self.__iSoulNumber = self.__reduceNumber(
            sum(self.__charToNum(ch) for ch in self.__name if ch in self.VOWEL_SET)
        )
        self.__iPersonalityNumber = self.__reduceNumber(
            sum(self.__charToNum(ch) for ch in self.__name if ch.isalpha() and ch not in self.VOWEL_SET)
        )
        self.__iPowerName = self.__reduceNumber(
            self.__iSoulNumber + self.__iPersonalityNumber
        )

    def __charToNum(self, ch):
        return ((ord(ch.upper()) - 65) % 9 + 1) if ch.isalpha() else 0
#reducing number single digit
    def __reduceNumber(self, num):
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num
#using property
    @property
    def Name(self):
        return self.__name

    @property
    def Birthdate(self):
        return self.__dob

    @property
    def LifePath(self):
        return self.__iLifePathNumber

    @property
    def BirthDay(self):
        return self.__iBirthdayNumber

    @property
    def Attitude(self):
        return self.__iAttitudeNumber

    @property
    def Soul(self):
        return self.__iSoulNumber

    @property
    def Personality(self):
        return self.__iPersonalityNumber

    @property
    def PowerName(self):
        return self.__iPowerName


class NumerologyLifePathDetails(Numerology):
    def __init__(self, sName, sDOB):
        super().__init__(sName, sDOB)
#life path descriptions
    @property
    def LifePathDescription(self):
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoys nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return descriptions.get(self.LifePath)

