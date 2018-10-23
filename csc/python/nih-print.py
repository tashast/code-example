def join(separator, sequence_of_strings):
    result = ''
    if not sequence_of_strings:
        return result
    for element in sequence_of_strings:
        result += '{}{}'.format(element, separator)
        len_sep = len(separator)
    if len_sep == 0:
        return result
    return result[:-len(separator)]

def print_to_string(*args, sep  = ' ', end = '\n'):
    sequence_of_strings = [item for item in args]
    result = join(sep, sequence_of_strings) + end
    return result