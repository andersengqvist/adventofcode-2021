import unittest

from src.day_18 import parse_snailfish_number,\
    add_snailfish_numbers,\
    parse_snailfish_numbers,\
    add_snailfish_number_list,\
    find_max_magnitude


class MyTestCase(unittest.TestCase):
    def test_parse_snailfish_number_1(self):
        (sf_number, idx) = parse_snailfish_number("[1,2]", 0)
        self.assertEqual(5, idx)
        self.assertEqual(1, sf_number.left())
        self.assertEqual(2, sf_number.right())
        self.assertEqual("[1,2]", str(sf_number))

    def test_parse_snailfish_number_2(self):
        (sf_number, idx) = parse_snailfish_number("[[1,2],3]", 0)
        self.assertEqual(9, idx)
        self.assertEqual(1, sf_number.left().left())
        self.assertEqual(2, sf_number.left().right())
        self.assertEqual(3, sf_number.right())
        self.assertEqual("[[1,2],3]", str(sf_number))

    def test_parse_snailfish_number_3(self):
        (sf_number, idx) = parse_snailfish_number("[9,[8,7]]", 0)
        self.assertEqual(9, idx)
        self.assertEqual(9, sf_number.left())
        self.assertEqual(8, sf_number.right().left())
        self.assertEqual(7, sf_number.right().right())
        self.assertEqual("[9,[8,7]]", str(sf_number))

    def test_parse_snailfish_number_4(self):
        (sf_number, idx) = parse_snailfish_number("[[1,9],[8,5]]", 0)
        self.assertEqual(13, idx)
        self.assertEqual(1, sf_number.left().left())
        self.assertEqual(9, sf_number.left().right())
        self.assertEqual(8, sf_number.right().left())
        self.assertEqual(5, sf_number.right().right())
        self.assertEqual("[[1,9],[8,5]]", str(sf_number))

    def test_parse_snailfish_number_5(self):
        (sf_number, idx) = parse_snailfish_number("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]", 0)
        self.assertEqual(1, sf_number.left().left().left().left())
        self.assertEqual(2, sf_number.left().left().left().right())
        self.assertEqual(3, sf_number.left().left().right().left())
        self.assertEqual(4, sf_number.left().left().right().right())
        self.assertEqual(5, sf_number.left().right().left().left())
        self.assertEqual(6, sf_number.left().right().left().right())
        self.assertEqual(7, sf_number.left().right().right().left())
        self.assertEqual(8, sf_number.left().right().right().right())
        self.assertEqual(9, sf_number.right())
        self.assertEqual("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]", str(sf_number))

    def test_parse_snailfish_number_6(self):
        (sf_number, idx) = parse_snailfish_number("[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]", 0)
        self.assertEqual("[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]", str(sf_number))

    def test_parse_snailfish_number_7(self):
        (sf_number, idx) = parse_snailfish_number("[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]", 0)
        self.assertEqual("[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]", str(sf_number))

    def test_add_snailfish_numbers(self):
        (sf1, idx) = parse_snailfish_number("[1,2]", 0)
        (sf2, idx) = parse_snailfish_number("[[3,4],5]", 0)
        sf3 = add_snailfish_numbers(sf1, sf2)
        self.assertEqual("[[1,2],[[3,4],5]]", str(sf3))

    def test_do_explode_1(self):
        # [[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4]
        # (the 9 has no regular number to its left, so it is not added to any regular number).
        (sf_number, idx) = parse_snailfish_number("[[[[[9,8],1],2],3],4]", 0)
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual((9, 0), p)
        self.assertEqual("[[[[0,9],2],3],4]", str(sf_number))

    def test_do_explode_2(self):
        # [7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]]
        # (the 2 has no regular number to its right, and so it is not added to any regular number).
        (sf_number, idx) = parse_snailfish_number("[7,[6,[5,[4,[3,2]]]]]", 0)
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual((0, 2), p)
        self.assertEqual("[7,[6,[5,[7,0]]]]", str(sf_number))

    def test_do_explode_3(self):
        # [[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
        (sf_number, idx) = parse_snailfish_number("[[6,[5,[4,[3,2]]]],1]", 0)
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual((0, 0), p)
        self.assertEqual("[[6,[5,[7,0]]],3]", str(sf_number))

    def test_do_explode_4(self):
        # [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
        # (the pair [3,2] is unaffected because the pair [7,3] is further to the left;
        # [3,2] would explode on the next action).
        (sf_number, idx) = parse_snailfish_number("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", 0)
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual((0, 0), p)
        self.assertEqual("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", str(sf_number))

    def test_do_explode_5(self):
        # [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
        (sf_number, idx) = parse_snailfish_number("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", 0)
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual((0, 2), p)
        self.assertEqual("[[3,[2,[8,0]]],[9,[5,[7,0]]]]", str(sf_number))

    def test_do_reduce_do_split(self):
        # after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
        # after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
        # after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
        # after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
        # after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
        # after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
        (sf_number, idx) = parse_snailfish_number("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", 0)
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]", str(sf_number))
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual("[[[[0,7],4],[15,[0,13]]],[1,1]]", str(sf_number))
        result = sf_number.do_split()
        self.assertTrue(result)
        self.assertEqual("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]", str(sf_number))
        result = sf_number.do_split()
        self.assertTrue(result)
        self.assertEqual("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]", str(sf_number))
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(3, result)
        self.assertEqual("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", str(sf_number))
        (result, p) = sf_number.do_explode(0)
        self.assertEqual(0, result)
        self.assertEqual("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", str(sf_number))
        result = sf_number.do_split()
        self.assertFalse(result)
        self.assertEqual("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", str(sf_number))

    def test_add_snailfish_number_list_1(self):
        the_input = ["[1,1]", "[2,2]", "[3,3]", "[4,4]"]
        sfs = parse_snailfish_numbers(the_input)
        result = add_snailfish_number_list(sfs)
        self.assertEqual("[[[[1,1],[2,2]],[3,3]],[4,4]]", str(result))

    def test_add_snailfish_number_list_2(self):
        the_input = ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"]
        sfs = parse_snailfish_numbers(the_input)
        result = add_snailfish_number_list(sfs)
        self.assertEqual("[[[[3,0],[5,3]],[4,4]],[5,5]]", str(result))

    def test_add_snailfish_number_list_3(self):
        the_input = ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"]
        sfs = parse_snailfish_numbers(the_input)
        result = add_snailfish_number_list(sfs)
        self.assertEqual("[[[[5,0],[7,4]],[5,5]],[6,6]]", str(result))

    def test_add_snailfish_number_list_4(self):
        the_input = [
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
            "[7,[5,[[3,8],[1,4]]]]",
            "[[2,[2,2]],[8,[8,1]]]",
            "[2,9]",
            "[1,[[[9,3],9],[[9,0],[0,7]]]]",
            "[[[5,[7,4]],7],1]",
            "[[[[4,2],2],6],[8,7]]"
        ]
        sfs = parse_snailfish_numbers(the_input)
        result = add_snailfish_number_list(sfs)
        self.assertEqual("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", str(result))

    def test_add_snailfish_number_list_5(self):
        the_input = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        sfs = parse_snailfish_numbers(the_input)
        result = add_snailfish_number_list(sfs)
        self.assertEqual("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", str(result))
        self.assertEqual(4140, result.magnitude())

    def test_magnitude(self):
        # The largest magnitude of the sum of any two snailfish numbers in this list is 3993.
        # This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        # + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
        # which reduces to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].
        (sf1, idx) = parse_snailfish_number("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]", 0)
        (sf2, idx) = parse_snailfish_number("[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]", 0)
        result = add_snailfish_numbers(sf1, sf2)
        self.assertEqual("[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]", str(result))
        self.assertEqual(3993, result.magnitude())

    def test_find_max_magnitude(self):
        the_input = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        sfs = parse_snailfish_numbers(the_input)
        result = find_max_magnitude(sfs)
        self.assertEqual(3993, result)


if __name__ == '__main__':
    unittest.main()
