import sys

LINES = [line for line in sys.stdin]

def print_set(some_set):
    if len(some_set) > 0:
        return ''.join(sorted(some_set))
    return '-'

ALL_LINES = set(''.join(LINES)) - {' ', '\n'}

prev = set()

if len(ALL_LINES) > 0:
    for line in LINES:
        curr_set = set(line) - {' ', '\n'}
        other = [set(other_line) for other_line in LINES if other_line != line]
        if len(other) > 1:
            other_set = other[0].union(*other[1:]) - {' ', '\n'}
        elif len(other) == 1:
            other_set = other[0] - {' ', '\n'}
        else:
            other_set = set()
        print(print_set(curr_set), print_set(curr_set - other_set), print_set(curr_set - prev), print_set(ALL_LINES - curr_set))
        prev = prev | curr_set
    print()

LINES_SET = [set(line) for line in LINES]
if len(LINES_SET) > 1:
    all_intersect = LINES_SET[0].intersection(*LINES_SET[1:])- {' ', '\n'}
elif len(LINES_SET) == 1:
    all_intersect = LINES_SET[0] - {' ', '\n'}
else:
    all_intersect = set()
print(print_set(all_intersect), print_set(ALL_LINES))
