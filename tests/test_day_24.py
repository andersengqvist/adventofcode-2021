import unittest
import math

from src.day_24 import Register, Alu, parse_program


class MyTestCase(unittest.TestCase):

    def test_it(self):
        self.assertEqual(2, math.trunc(5/2))
        self.assertEqual(-2, math.trunc(-5/2))

    def test_register(self):
        register = Register()
        self.assertEqual(0, register.get("w"))
        register.set("w", 33)
        self.assertEqual(33, register.get("w"))

    def test_run_program_1(self):
        the_input = [
            "inp x",
            "mul x -1"
        ]
        program = parse_program(the_input)
        alu = Alu()
        register = alu.run(program, [7])
        self.assertEqual(-7, register.get("x"))

    def test_run_program_2(self):
        the_input = [
            "inp z",
            "inp x",
            "mul z 3",
            "eql z x"
        ]
        program = parse_program(the_input)
        alu = Alu()
        register = alu.run(program, [7, 21])
        self.assertEqual(1, register.get("z"))


if __name__ == '__main__':
    unittest.main()
