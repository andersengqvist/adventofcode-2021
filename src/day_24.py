from lib.files import read_lines
import math


# Wow...
# What a day.
# Started with implementing the Alu, but realized that it would take a long time to brute force.
# So started looking at the input, and slowly transformed it to what can be seen in day_24_3.txt
# In day_24_2.txt the operations had been grouped together to make sense of them
# For z to ever be 0 we must divide it by 26 on every instance of this:
# sp4 a _ # x = 1 if (z % 26) + a != w else 0
# sp3 26 b # z = (z / 26) * (25 * x + 1) + x * (w + b)
# And the only way that can happen is if x == 0
# Then the operations simply becomes:
# z = z / 26
# And when ever x becomes 1 we can make the search space smaller.
# For example, the first check happens after the fifth digit has been read into w.
# And if that is wrong, we do not need to check digit 5-14, and can check the next digit at position 5 directly
# So created the AluBreaker for this new set of instructions and set it to work.
# Took some time, but eventually it gave an answer.
# There probably are some more clever stuff that can be done to limit the search space, but I cannot see anything.
#
# ... wait ..., there is a relation between them:
# The first digit read into w (w0) has a relation with the last digit (w13):
# First z is set to w0 + 14, and that is the value we will have on the last modulo when we have read w13 into w
# So (z % 26) = w0 + 14
# And w0 + 14 - 9 (w0 + 5) must equal to w13
# And because both w0 and w13 is between 1 and 9, w0 must be at least 1 and at most 5,
# w13 is at least 1 + 5 = 6 and at most 4 + 5 = 9
#
# By doing this for all w0-w13 we have a lower and upper bound of all the digits in the model number,
# and also the solution to the two questions!
# To find the highest number just take the upper bound on each digit, and to find the lowest then take the lower bound:
# w0  = [1 4]
# w1  = [1 5]
# w2  = [9 9]
# w3  = [1 8]
# w4  = [2 9]
# w5  = [8 9]
# w6  = [1 2]
# w7  = [4 9]
# w8  = [6 9]
# w9  = [1 4]
# w10 = [1 6]
# w11 = [1 1]
# w12 = [5 9]
# w13 = [6 9]

def part1():
    # the_input1 = read_lines("res/day_24_1.txt")
    # program1 = parse_program(the_input1)
    # alu = Alu()
    # model_number = "45989929946199"
    # res = alu.run(program1, [int(s) for s in model_number])
    # print(str(res))

    # the_input3 = read_lines("res/day_24_3.txt")
    # program3 = parse_program(the_input3)
    # ab = AluBreaker()
    # res = ab.find_high(program3)
    res = 45989929946199
    print("Day 24.1: {}".format(res))


def part2():
    # the_input1 = read_lines("res/day_24_1.txt")
    # program1 = parse_program(the_input1)
    # alu = Alu()
    # model_number = "11912814611156"
    # res = alu.run(program1, [int(s) for s in model_number])
    # print(str(res))

    # the_input3 = read_lines("res/day_24_3.txt")
    # program3 = parse_program(the_input3)
    # ab = AluBreaker()
    # res = ab.find_low(program3)
    res = 11912814611156
    print("Day 24.2: {}".format(res))


class Register:
    def __init__(self):
        self._reg = [0, 0, 0, 0]

    def set(self, ch, val):
        self._reg[ord(ch) - 119] = val

    def get(self, ch):
        i = ord(ch[0])
        if i >= 119:
            return self._reg[i - 119]
        return int(ch)

    def __repr__(self):
        return "w: {}, x: {}, y: {}, z: {}".format(self._reg[0], self._reg[1], self._reg[2], self._reg[3])


class Alu:
    def run(self, program, model_number):
        register = Register()
        mod_idx = 0
        for ins in program:
            if ins[0] == "inp":
                input_val = model_number[mod_idx]
                mod_idx += 1
                register.set(ins[1], input_val)
            elif ins[0] == "add":
                register.set(ins[1], register.get(ins[1]) + register.get(ins[2]))
            elif ins[0] == "mul":
                register.set(ins[1], register.get(ins[1]) * register.get(ins[2]))
            elif ins[0] == "div":
                register.set(ins[1], math.trunc(register.get(ins[1]) / register.get(ins[2])))
            elif ins[0] == "mod":
                register.set(ins[1], register.get(ins[1]) % register.get(ins[2]))
            elif ins[0] == "eql":
                register.set(ins[1], 1 if register.get(ins[1]) == register.get(ins[2]) else 0)
            elif ins[0] == "sp1":
                # z = z * (25 * x + 1)
                register.set("z", register.get("z") * (25 * register.get("x") + 1))
            elif ins[0] == "sp2":
                # z = z + x * (w + a)
                register.set("z", register.get("z") + register.get("x") * (register.get("w") + int(ins[1])))
            elif ins[0] == "sp3":
                # z = (z / a) * (25 * x + 1) + x * (w + b)
                z = register.get("z")
                x = register.get("x")
                w = register.get("w")
                register.set("z", math.trunc(z / int(ins[1])) * (25 * x + 1) + x * (w + int(ins[2])))
            elif ins[0] == "sp4":
                # x = 1 if (z % 26) + a != w else 0
                register.set("x", 1 if (register.get("z") % 26) + int(ins[1]) != register.get("w") else 0)
            else:
                raise Exception("Unknown operator: {}".format(ins[0]))
        return register


class ModelNumber:
    def __init__(self, the_size, digit):
        self._mn = [digit for _i in range(the_size)]

    def inc(self, idx):
        if idx < 0 or idx >= len(self._mn):
            raise Exception("Trying to increase invalid index {} of number: {}".format(idx, str(self)))
        self._mn[idx] += 1
        if self._mn[idx] > 9:
            self._mn[idx] = 1
            self.inc(idx - 1)

    def dec(self, idx):
        if idx < 0 or idx >= len(self._mn):
            raise Exception("Trying to decrease invalid index {} of number: {}".format(idx, str(self)))
        self._mn[idx] -= 1
        if self._mn[idx] < 1:
            self._mn[idx] = 9
            self.dec(idx - 1)

    def model_number(self):
        return self._mn

    def __repr__(self):
        return "".join(str(i) for i in self._mn)


class AluBreaker:
    def __init__(self):
        pass

    def find_high(self, program):
        mn = ModelNumber(14, 9)
        while True:
            idx = self.run(program, mn.model_number())
            if idx >= 0:
                mn.dec(idx)
            else:
                return mn

    def find_low(self, program):
        mn = ModelNumber(14, 1)
        while True:
            idx = self.run(program, mn.model_number())
            if idx >= 0:
                mn.inc(idx)
            else:
                return mn

    def run(self, program, model_number):
        w = 0
        z = 0
        mod_idx = 0
        for ins in program:
            if ins[0] == "inp":
                w = model_number[mod_idx]
                mod_idx += 1
            elif ins[0] == "br1":
                z = z * 26 + w + int(ins[1])
            elif ins[0] == "br2":
                if (z % 26) + int(ins[1]) != w:
                    return mod_idx - 1
            elif ins[0] == "br3":
                z = math.trunc(z / 26)
            else:
                raise Exception("Unknown operator: {}".format(ins[0]))
        if z == 0:
            return -1
        else:
            return mod_idx - 1


def parse_program(the_input):
    return [line.split() for line in the_input]


if __name__ == "__main__":
    part1()
    part2()
