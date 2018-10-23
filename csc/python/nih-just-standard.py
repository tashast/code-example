def ljust(string, width, fillchar):
    fills = fillchar * (width - len(string))
    return string + fills

def rjust(string, width, fillchar):
    fills = fillchar * (width - len(string))
    return fills + string

def center(string, width, fillchar):
    width -= len(string)
    width_1 = width // 2
    width_2 = width - width_1
    return fillchar * width_1 + string + fillchar * width_2