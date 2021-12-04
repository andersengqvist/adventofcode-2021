
def read_lines(the_file):
    """
    Read file lines into list of strings, leading and trailing whitespace removed (including new line)
    :param the_file: the file to read
    :return: list of strings of the file lines
    """
    with open(the_file) as fp:
        return [line.strip() for line in fp.readlines()]


def read_file(the_file):
    """
    Read entire file into a string
    :param the_file: the file to read
    :return: a string with the file content
    """
    with open(the_file) as fp:
        return fp.read()
