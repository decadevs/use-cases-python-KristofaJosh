# Document at least 3 use cases of static methods

from datetime import date


class Test:
    def __init__(self, yob):
        self.yob = yob

    def calc_age(self):
        age = self.get_age(self.yob)
        return age

    def calc_korean_age(self):
        year = self.korean_age(self.yob)
        return year

    @staticmethod
    def get_age(yob):
        """Uses year of birth to determine age"""
        try:
            return f'You are {date.today().year - yob} years old'
        except TypeError:
            raise TypeError

    @staticmethod
    def korean_age(yob):
        try:
            return f'Your korean age is {date.today().year - yob + 3}'
        except TypeError:
            raise TypeError

    @staticmethod
    def about():
        return  'This is just an illustration of static methods'






test = Test(1992)
print(test.calc_age())
print(test.calc_korean_age())
print(test.about())