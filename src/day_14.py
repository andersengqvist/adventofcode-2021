from lib.files import read_file
from collections import Counter
import os


def part1():
    the_input = read_file("res/day_14_1.txt")
    res = solve_part(the_input, 10)
    print("Day 14.1: {}".format(res))


def part2():
    the_input = read_file("res/day_14_1.txt")
    res = solve_part(the_input, 40)
    print("Day 14.2: {}".format(res))


def parse_input(the_input):
    chunks = the_input.split(os.linesep + os.linesep)
    polymer = build_polymer(chunks[0])
    rules = build_rules(chunks[1])
    return chunks[0], polymer, rules


def build_polymer(param):
    # The polymer is a Counter for the pairs in the input string
    counter = Counter()
    for i in range(len(param) - 1):
        pair = param[i:i + 2]
        counter[pair] += 1
    return counter


def build_rules(param):
    # The rules maps a pair to two new pairs
    # For example: {PH: (PV, VH)}
    lines = param.split(os.linesep)
    rules = dict()
    for line in lines:
        ls = line.strip()
        if ls:
            key = ls[0:2]
            new_char = ls[6:7]
            pair1 = ls[0:1] + new_char
            pair2 = new_char + ls[1:2]
            rules[key] = (pair1, pair2)
    return rules


def run_steps(polymer, rules, steps):
    p = polymer
    for step in range(steps):
        p = run_step(p, rules)
    return p


def run_step(polymer, rules):
    # Takes the polymer, run the rules and returns a new polymer
    # Example: for polymer of {PH: 1} and rules {PH: (PV, VH)}, the result will be {PV: 1, VH: 1}
    # Assumes all pairs are in the rules
    next_polymer = Counter()
    for (elem, cnt) in polymer.items():
        pair = rules[elem]
        next_polymer[pair[0]] += cnt
        next_polymer[pair[1]] += cnt
    return next_polymer


def get_elements(original_polymer, polymer):
    # This is a bit tricky:
    # The polymer contains pairs, but the second char of one pair is the first of another pair
    # So we only count the first char, but then we miss the last in the polymer "String"
    # that is why we need the original polymer string, to fetch the last char and att the count for that with one.
    # There will never be a different char at the end,
    # no matter how many times the rules are applied, because a char is always inserted between two chars.
    counter = Counter()
    for (elem, cnt) in polymer.items():
        counter[elem[0]] += cnt
    last_elem = original_polymer[-1]
    counter[last_elem] += 1
    return counter


def solve_part(the_input, steps):
    (original_polymer, polymer, rules) = parse_input(the_input)
    resulting_polymer = run_steps(polymer, rules, steps)
    elements = get_elements(original_polymer, resulting_polymer)
    all_sorted = elements.most_common()
    most_common = all_sorted[0]
    least_common = all_sorted[-1]
    return most_common[1] - least_common[1]


if __name__ == "__main__":
    part1()
    part2()
