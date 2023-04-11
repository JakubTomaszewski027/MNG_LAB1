import unittest

from mail import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "norbert", "waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "jan", "kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "anna", "nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "adrianna", "abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "katarzyna", "babacka"],

            ["marek.jarecki@student.wat.edu.pl", True, True, "marek", "jarecki"],
            ["weronika.jankowska@wat.edu.pl", False, False, "weronika", "jankowska"],
            ["aleksandra.buczkowska@wat.edu.pl", False, True, "aleksandra", "buczkowska"],
            ["alicja.kaminska01@student.wat.edu.pl", True, False, "alicja", "kaminska"],
            ["anastazja.laskowska@wat.edu.pl", False, False, "anastazja", "laskowska"],
            ["baltazar.gabka@wat.edu.pl", False, True, "baltazar", "gabka"],
            ["klaudia.rudzka@student.wat.edu.pl", True, False, "klaudia", "rudzka"],
            ["dominik.mlynarski02@student.wat.edu.pl", True, True, "dominik", "mlynarski"],
            ["konstanty.malinowski@wat.edu.pl", False, True, "konstanty", "malinowski"],
            ["dawid.jasper@student.wat.edu.pl", True, True, "dawid", "jasper"],
        ]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())
