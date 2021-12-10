import unittest

from src.day_10 import Line, get_total_syntax_error, get_middle_score

the_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]"
]


class MyTestCase(unittest.TestCase):
    def test_corrupt_lines(self):
        line = Line("{([(<{}[<>[]}>{[]{[(<()>")
        self.assertTrue(line.is_corrupted())
        self.assertEqual(1197, line.get_points())
        line = Line("[[<[([]))<([[{}[[()]]]")
        self.assertTrue(line.is_corrupted())
        self.assertEqual(3, line.get_points())
        line = Line("[{[{({}]{}}([{[{{{}}([]")
        self.assertTrue(line.is_corrupted())
        self.assertEqual(57, line.get_points())
        line = Line("[<(<(<(<{}))><([]([]()")
        self.assertTrue(line.is_corrupted())
        self.assertEqual(3, line.get_points())
        line = Line("<{([([[(<>()){}]>(<<{{")
        self.assertTrue(line.is_corrupted())
        self.assertEqual(25137, line.get_points())

    def test_get_total_syntax_error(self):
        self.assertEqual(26397, get_total_syntax_error(the_input))

    def test_incomplete_lines(self):
        line = Line("[({(<(())[]>[[{[]{<()<>>")
        self.assertTrue(line.is_incomplete())
        self.assertEqual(288957, line.get_points())
        line = Line("[(()[<>])]({[<{<<[]>>(")
        self.assertTrue(line.is_incomplete())
        self.assertEqual(5566, line.get_points())
        line = Line("(((({<>}<{<{<>}{[]{[]{}")
        self.assertTrue(line.is_incomplete())
        self.assertEqual(1480781, line.get_points())
        line = Line("{<[[]]>}<{[{[{[]{()[[[]")
        self.assertTrue(line.is_incomplete())
        self.assertEqual(995444, line.get_points())
        line = Line("<{([{{}}[<[[[<>{}]]]>[]]")
        self.assertTrue(line.is_incomplete())
        self.assertEqual(294, line.get_points())

    def test_get_middle_score(self):
        self.assertEqual(288957, get_middle_score(the_input))


if __name__ == '__main__':
    unittest.main()
