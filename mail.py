import re


class EmailExtractor:

    def __init__(self, email):
        self.email = email
        self.regex = r"(?P<name>[a-z]+)\.(?P<surname>[a-z]+)[0-9]*@(?P<is_student>(student\.)?)(wat\.edu\.pl)"

    def get_name(self):
        x = re.compile(self.regex)
        y = x.findall(self.email)
        name = y[0][1]
        return name

    def get_surname(self):
        x = re.compile(self.regex)
        y = x.findall(self.email)
        surname = y[0][1]
        return surname

    def is_student(self) -> bool:
        x = re.compile(self.regex)
        y = x.findall(self.email)
        if y[0][3] == "":
            return False
        else:
            return True

    def is_male(self) -> bool:
        name = self.get_name()
        x = name[-1]
        if x == "a":
            return False
        else:
            return True
