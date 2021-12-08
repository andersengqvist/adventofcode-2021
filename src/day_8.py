from lib.files import read_lines


def part1():
    the_input = read_lines("res/day_8_1.txt")
    res = count_unique_number_of_segments(the_input)
    print("Day 8.1: {}".format(res))


def part2():
    the_input = read_lines("res/day_8_1.txt")
    res = sum_outputs(the_input)
    print("Day 8.2: {}".format(res))


def count_unique_number_of_segments(the_input):
    outputs = [output for line in the_input for output in get_output_values(line)]
    res = 0
    for output in outputs:
        ln = len(output)
        if ln == 2 or ln == 3 or ln == 4 or ln == 7:
            res += 1
    return res


def get_output_values(line):
    return [p.strip() for p in line.split("|")[1].split() if p.strip()]


def sum_outputs(the_input):
    return sum(sum_output(line) for line in the_input)


def sum_output(line):
    parsed = parse_line(line)
    digit_map = find_digits(parsed[0])
    return get_output(parsed[1], digit_map)


def parse_line(line):
    splitted = line.split("|")

    tmp1 = (p.strip() for p in splitted[0].split() if p.strip())
    tmp2 = [frozenset(p) for p in tmp1]

    tmp3 = (p.strip() for p in splitted[1].split() if p.strip())
    tmp4 = [frozenset(p) for p in tmp3]

    return tmp2, tmp4

# Number, Num Segments, Segments, Calculation
# 0       6             abc_efg   Only 6 segment number left after 6 and 9 is removed
# 1       2             __c__f_   Only 2 segment number
# 2       5             a_cde_g   Only 5 segment number left after 3 and 5 is removed
# 3       5             a_cd_fg   7 subset 3, Only 5 segment number that contains all segments of 7
# 4       4             _bcd_f_   Only 4 segment number
# 5       5             ab_d_fg   5 subset 6, Only 5 segment number that contain all segments of 6
# 6       6             ab_defg   1 & 6 == 1, only 6 segment number that shares 1 segment with 1
# 7       3             a_c__f_   Only 3 segment number
# 8       7             abcdefg   Only 7 segment number
# 9       6             abcd_fg   4 subset 9, 9 is only 6 segment number that contain all segments of 4


def find_digits(segment_list):
    the_map = {}
    segment_list = find_1(segment_list, the_map)
    segment_list = find_4(segment_list, the_map)
    segment_list = find_7(segment_list, the_map)
    segment_list = find_8(segment_list, the_map)
    segment_list = find_6(segment_list, the_map)
    segment_list = find_9(segment_list, the_map)
    segment_list = find_0(segment_list, the_map)
    segment_list = find_5(segment_list, the_map)
    segment_list = find_3(segment_list, the_map)
    find_2(segment_list, the_map)

    return dict((v, k) for k, v in the_map.items())


def find_num_with_len(seg_list, the_map, the_num, the_len):
    res = []
    for seg in seg_list:
        if len(seg) == the_len:
            the_map.update({the_num: seg})
        else:
            res.append(seg)
    return res


def find_1(seg_list, the_map):
    return find_num_with_len(seg_list, the_map, 1, 2)


def find_4(seg_list, the_map):
    return find_num_with_len(seg_list, the_map, 4, 4)


def find_7(seg_list, the_map):
    return find_num_with_len(seg_list, the_map, 7, 3)


def find_8(seg_list, the_map):
    return find_num_with_len(seg_list, the_map, 8, 7)


def find_6(seg_list, the_map):
    one = the_map[1]

    res = []
    for seg in seg_list:
        if len(seg) == 6 and len(one & seg) == 1:
            the_map.update({6: seg})
        else:
            res.append(seg)
    return res


def find_9(seg_list, the_map):
    four = the_map[4]

    res = []
    for seg in seg_list:
        if len(seg) == 6 and four.issubset(seg):
            the_map.update({9: seg})
        else:
            res.append(seg)
    return res


def find_0(seg_list, the_map):
    return find_num_with_len(seg_list, the_map, 0, 6)


def find_5(seg_list, the_map):
    six = the_map[6]

    res = []
    for seg in seg_list:
        if len(seg) == 5 and seg.issubset(six):
            the_map.update({5: seg})
        else:
            res.append(seg)
    return res


def find_3(seg_list, the_map):
    seven = the_map[7]

    res = []
    for seg in seg_list:
        if len(seg) == 5 and seven.issubset(seg):
            the_map.update({3: seg})
        else:
            res.append(seg)
    return res


def find_2(seg_list, the_map):
    return find_num_with_len(seg_list, the_map, 2, 5)


def get_output(output, digit_map):
    res = 0
    for seg in output:
        digit = digit_map[seg]
        res = res * 10 + digit
    return res


if __name__ == "__main__":
    part1()
    part2()
