import re

class EmailExtractor:

    def __init__(self, emailD: str):
        self.email = emailD
        self.regex = r"(?P<name>[a-z]+)\.(?P<surname>[a-z]+)[0-9]*@(?P<is_student>(student\.)?)(wat\.edu\.pl)"

    def is_student(self) -> bool:
        x = re.compile("")
        x.match(self.email)
        return False

    def is_male(self) -> bool:
        return False

    def get_name(self) -> str:
        return "Norbert"

    def get_surname(self) -> str:
        return "Waszkowiak"



