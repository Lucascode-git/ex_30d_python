age = 25
height = 1.77
complex = 18.854

#base = float(input('Enter base: '))
#tri_height = float(input('Enter height: '))
#print(f'The area of the triangle is {(base*tri_height)/2:.2f}')

# EX 6 rectangle
#rect_length = float(input('Enter length: '))
#rect_width = float(input('Enter width: '))
#print(f'The area of the rectangle is {rect_length * rect_width:.2f}')
#print(f'The perimeter of the rectangle is {2 * (rect_length + rect_width):.2f}')

#EX 7
#raduis = float(input('Enter raduis: '))
#pi = 3.14
#print(f'The area of the circle is {pi * raduis * raduis:.2f}')
#print(f'The circumference of the circle is {2 * pi * raduis:.2f}')

#EX8
# y = 2x - 2
m = 2
b = -2

slope1 = m
y_intercept1 = b
x_intercept1 = -b / m

print(f'\nSlope1: {slope1}')
print(f'x-intercept: {x_intercept1}')
print(f'y-intercept: {y_intercept1}\n')

#EX9
#Slope m = (y2-y1)/(x2-x1)
y1 = 2
y2 = 10
x1 = 2
x2 = 6
m = (y2-y1)/(x2-x1)
print(f'Slope2: {m}')

xdiff = x2 - x1
ydiff = y2 - y1
sum_xy_square = xdiff **2 + ydiff ** 2
eucli_dist = sum_xy_square ** 0.5
print(f'Euclidean distance: {eucli_dist:.2f}\n')

#EX11
x = -3
y = x**2 + 6*x +9
print(f'for x={x} -> y={y}\n')

#EX12
len_python = len('python')
len_dragon = len('dragon')
print(len_python > len_dragon)
print()

sentence_jargon = 'I hope this course is not full of jargon'
print('jargon' in sentence_jargon)
print()

print('on' not in 'dragon' and 'on' not in 'python')
print()

print(len_python)
float_python = float(len_python)
print(float_python)
str_python = str(float_python)
print(str_python)
print()

number = 10
even_test = number % 2
if even_test == 0:
    print('EVEN number')
else:
    print('ODD number')
print()

ref_value = 2.7
converted_value = int(ref_value)

calcul_floor = 7 // 3
print(calcul_floor == converted_value)
print('-------------')

print('10' == 10)
print('-------------')

print(int(9.8) == 10)
print('-------------')

#hours = float(input('Enter hours: '))
#rate = float(input('Enter rate per hour: '))
#print(f'Your weekly earining is: {hours*rate:.2f}€')

#lived_years = float(input('Enter number of years you have lived: '))
#print(f'You have lived for: {(lived_years * 31536.000):,} seconds')

#23
a = 1
b = 2
c = 3
d = 4
e = 5

print(a, int(a/a), a*1, a*a, a**3)
print(b, int(b/b), b*1, b*b, b**3)
print(c, int(c/c), c*1, c*c, c**3)
print(d, int(d/d), d*1, d*d, d**3)
print(e, int(e/e), e*1, e*e, e**3)