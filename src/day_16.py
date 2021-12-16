from lib.files import read_file


def part1():
    the_input = read_file("res/day_16_1.txt").strip()
    bin_str = hex_str_to_binary_str(the_input)
    (_idx, packet) = parse_packet(bin_str, 0)
    res = packet.version_sum()
    print("Day 16.1: {}".format(res))


def part2():
    the_input = read_file("res/day_16_1.txt")
    bin_str = hex_str_to_binary_str(the_input)
    (_idx, packet) = parse_packet(bin_str, 0)
    res = packet.value()
    print("Day 16.2: {}".format(res))


def hex_str_to_binary_str(hex_str):
    # https://stackoverflow.com/questions/1425493/convert-hex-to-binary/28913296#28913296
    # Copied, do not understand
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


class Packet:
    def __init__(self, version, type_id):
        self._version = version
        self._type_id = type_id

    def version(self):
        return self._version

    def type_id(self):
        return self._type_id


class LiteralValue(Packet):
    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self._value = value

    def value(self):
        return self._value

    def version_sum(self):
        return self.version()


class Operator(Packet):
    def __init__(self, version, type_id, packets):
        super().__init__(version, type_id)
        self._packets = packets

    def packets(self):
        return self._packets

    def version_sum(self):
        res = 0
        for p in self._packets:
            res += p.version_sum()
        return self.version() + res

    def value(self):
        if self.type_id() == 0:
            return sum(p.value() for p in self._packets)
        elif self.type_id() == 1:
            res = 1
            for p in self._packets:
                res *= p.value()
            return res
        elif self.type_id() == 2:
            return min(p.value() for p in self._packets)
        elif self.type_id() == 3:
            return max(p.value() for p in self._packets)
        elif self.type_id() == 5:
            if self._packets[0].value() > self._packets[1].value():
                return 1
            else:
                return 0
        elif self.type_id() == 6:
            if self._packets[0].value() < self._packets[1].value():
                return 1
            else:
                return 0
        elif self.type_id() == 7:
            if self._packets[0].value() == self._packets[1].value():
                return 1
            else:
                return 0


def parse_packet(the_str, begin_idx):
    idx = begin_idx
    version = int(the_str[idx: idx + 3], 2)
    idx += 3
    type_id = int(the_str[idx: idx + 3], 2)
    idx += 3
    if type_id == 4:
        return parse_literal(the_str, idx, version, type_id)
    else:
        length_type_id = the_str[idx: idx + 1]
        idx += 1
        packets = []
        if length_type_id == "0":
            total_length = int(the_str[idx: idx + 15], 2)
            idx += 15
            stop = idx + total_length
            while idx < stop:
                (idx, packet) = parse_packet(the_str, idx)
                packets.append(packet)
        else:
            num_sub_packets = int(the_str[idx: idx + 11], 2)
            idx += 11
            for _i in range(num_sub_packets):
                (idx, packet) = parse_packet(the_str, idx)
                packets.append(packet)
        return idx, Operator(version, type_id, packets)


def parse_literal(the_str, begin_idx, version, type_id):
    idx = begin_idx
    result = ""
    while the_str[idx] == "1":
        result += the_str[idx + 1: idx + 5]
        idx += 5
    result += the_str[idx + 1: idx + 5]
    idx += 5
    value = int(result, 2)
    return idx, LiteralValue(version, type_id, value)


if __name__ == "__main__":
    part1()
    part2()
