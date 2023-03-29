import unittest

from mail import EmailExtractor

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],

            ["marek.jarecki@student.wat.edu.pl", True, True, "Marek", "Jarecki"],
            ["weronika.jankowska@wat.edu.pl", False, False, "Weronika", "Jankowska"],
            ["aleksandra.buczkowska@wat.edu.pl", False, True, "Aleksandra", "Buczkowska"],
            ["alicja.kaminska01@student.wat.edu.pl", True, False, "Alicja", "Kaminska"],
            ["anastazja.laskowska@wat.edu.pl", False, False, "Anastazja", "Laskowska"],
            ["baltazar.gabka@wat.edu.pl", False, True, "Baltazar", "Gabka"],
            ["klaudia.rudzka@student.wat.edu.pl", True, False, "Klaudia", "Rudzka"],
            ["dominik.mlynarski02@student.wat.edu.pl", True, True, "Dominik", "Mlynarski"],
            ["konstanty.malinowski@wat.edu.pl", False, True, "Konstanty", "Malinowski"],
            ["dawid.jasper@student.wat.edu.pl", True, True, "Dawid", "Jasper"],
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
            with self.subTest(): to
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
