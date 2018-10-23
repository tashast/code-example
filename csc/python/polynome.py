import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-a', type=float, action='store', nargs='+', help='list of coefficients')
parser.add_argument('-x', type=float, action='store', nargs=1, help='variable x')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose flag')

args = parser.parse_args()

coeff = args.a
degree = len(coeff)-1
x_var = args.x[0]
p = 0
str_out = ''
for i in range(degree):
    p += coeff[i] * x_var ** (degree-i)
    str_out += str(coeff[i]) + '*' + str(x_var ** (degree-i))+'+'

p += coeff[-1]
str_out += str(coeff[-1]) + '*1.0=' + str(p)

if args.verbose:
    print(str_out)
else:
    print(p)
