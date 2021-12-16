import unittest

from src.day_16 import hex_str_to_binary_str, parse_packet


class MyTestCase(unittest.TestCase):

    def test_hex_str_to_binary_str(self):
        self.assertEqual("110100101111111000101000", hex_str_to_binary_str("D2FE28"))
        self.assertEqual("00111000000000000110111101000101001010010001001000000000", hex_str_to_binary_str("38006F45291200"))
        self.assertEqual("11101110000000001101010000001100100000100011000001100000", hex_str_to_binary_str("EE00D40C823060"))

    def test_parse_value_packet(self):
        (idx, packet) = parse_packet("110100101111111000101000", 0)
        self.assertEqual(21, idx)
        self.assertEqual(6, packet.version())
        self.assertEqual(4, packet.type_id())
        self.assertEqual(2021, packet.value())

    def test_parse_operator_packet1(self):
        (idx, packet) = parse_packet("00111000000000000110111101000101001010010001001000000000", 0)
        self.assertEqual(49, idx)
        self.assertEqual(1, packet.version())
        self.assertEqual(6, packet.type_id())
        children = packet.packets()
        self.assertEqual(10, children[0].value())
        self.assertEqual(20, children[1].value())

    def test_parse_operator_packet2(self):
        (idx, packet) = parse_packet("11101110000000001101010000001100100000100011000001100000", 0)
        self.assertEqual(51, idx)
        self.assertEqual(7, packet.version())
        self.assertEqual(3, packet.type_id())
        children = packet.packets()
        self.assertEqual(1, children[0].value())
        self.assertEqual(2, children[1].value())
        self.assertEqual(3, children[2].value())

    def test_sum_version1(self):
        bin_str = hex_str_to_binary_str("8A004A801A8002F478")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(16, packet.version_sum())

    def test_sum_version2(self):
        bin_str = hex_str_to_binary_str("620080001611562C8802118E34")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(12, packet.version_sum())

    def test_sum_version3(self):
        bin_str = hex_str_to_binary_str("C0015000016115A2E0802F182340")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(23, packet.version_sum())

    def test_sum_version4(self):
        bin_str = hex_str_to_binary_str("A0016C880162017C3686B18A3D4780")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(31, packet.version_sum())

    def test_value1(self):
        bin_str = hex_str_to_binary_str("C200B40A82")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(3, packet.value())

    def test_value2(self):
        bin_str = hex_str_to_binary_str("04005AC33890")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(54, packet.value())

    def test_value3(self):
        bin_str = hex_str_to_binary_str("880086C3E88112")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(7, packet.value())

    def test_value4(self):
        bin_str = hex_str_to_binary_str("CE00C43D881120")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(9, packet.value())

    def test_value5(self):
        bin_str = hex_str_to_binary_str("D8005AC2A8F0")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(1, packet.value())

    def test_value6(self):
        bin_str = hex_str_to_binary_str("F600BC2D8F")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(0, packet.value())

    def test_value7(self):
        bin_str = hex_str_to_binary_str("9C005AC2F8F0")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(0, packet.value())

    def test_value8(self):
        bin_str = hex_str_to_binary_str("9C0141080250320F1802104A08")
        (idx, packet) = parse_packet(bin_str, 0)
        self.assertEqual(1, packet.value())


if __name__ == '__main__':
    unittest.main()
