def ljust(string, width, rights):
    if rights == '':
        rights = ' '
    width_residue = (width - len(string)) % len(rights)
    if width_residue == 0:
        return string + rights * ((width - len(string)) // len(rights))
    rights_residue = rights[-width_residue:]
    return string + rights_residue + rights * ((width - len(string)) // len(rights))

def rjust(string, width, lefts):
    if lefts == '':
        lefts = ' '
    width_residue = (width - len(string)) % len(lefts)
    if width_residue == 0:
        return lefts * ((width - len(string)) // len(lefts)) + string
    lefts_residue = lefts[:width_residue]
    return lefts * ((width - len(string)) // len(lefts)) + lefts_residue + string

def center(string, width, lefts, rights):
    if rights == '':
        rights = ' '
    if lefts == '':
        lefts = ' '
    width_other = width - len(string)
    if width_other % 2 == 0:
        string_result = ljust(string, (len(string) + width_other //2), rights)
        string_result = rjust(string_result, (len(string_result) + width_other //2), lefts)
        return string_result
    width_small = width_other // 2
    if width_small % len(lefts) == 0 and (width_small + 1) % len(rights) == 0:
        string_result = ljust(string, len(string) + width_small + 1, rights)
        string_result = rjust(string_result, len(string_result) + width_small, lefts)
        return string_result
    if width_small % len(rights) == 0 and (width_small + 1) % len(lefts) == 0:
        string_result = ljust(string, len(string) + width_small, rights)
        string_result = rjust(string_result, len(string_result) + width_small + 1, lefts)
        return string_result
    diff_lefts = width_small % len(lefts) + (width_small + 1) % len(rights)
    diff_rights = (width_small + 1) % len(lefts) + width_small % len(rights)
    if diff_rights < diff_lefts:
        string_result = ljust(string, len(string) + width_small, rights)
        string_result = rjust(string_result, len(string_result) + width_small + 1, lefts)
        return string_result
    else:
        string_result = ljust(string, len(string) + width_small + 1, rights)
        string_result = rjust(string_result, len(string_result) + width_small, lefts)
        return string_result
    return