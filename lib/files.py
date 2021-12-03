
def read_lines(the_file):
    with open(the_file) as fp:
        return [line.strip() for line in fp.readlines()]
