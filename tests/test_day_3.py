import unittest

from src.day_3 import get_gamma_and_epsilon, oxygen_generator_rating, co2_scrubber_rating


class MyTestCase(unittest.TestCase):
    def test_get_gamma_and_epsilon(self):
        self.assertEqual((22, 9), get_gamma_and_epsilon(["00100",
                                                         "11110",
                                                         "10110",
                                                         "10111",
                                                         "10101",
                                                         "01111",
                                                         "00111",
                                                         "11100",
                                                         "10000",
                                                         "11001",
                                                         "00010",
                                                         "01010"]))

    def test_oxygen_generator_rating(self):
        self.assertEqual(23, oxygen_generator_rating(["00100",
                                                      "11110",
                                                      "10110",
                                                      "10111",
                                                      "10101",
                                                      "01111",
                                                      "00111",
                                                      "11100",
                                                      "10000",
                                                      "11001",
                                                      "00010",
                                                      "01010"]))

    def test_co2_scrubber_rating(self):
        self.assertEqual(10, co2_scrubber_rating(["00100",
                                                  "11110",
                                                  "10110",
                                                  "10111",
                                                  "10101",
                                                  "01111",
                                                  "00111",
                                                  "11100",
                                                  "10000",
                                                  "11001",
                                                  "00010",
                                                  "01010"]))


if __name__ == '__main__':
    unittest.main()
