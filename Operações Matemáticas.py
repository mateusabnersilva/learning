#Operações Matemáticas

num1 = 56
num2 = -4

print(type(num1))
print(type(num2))

num3 = 60 
num4 = 12

soma = num3 + num4
print('Integer Addition:', soma)

num5 = 56
num6 = 12

sub = num5 - num6 
print('Integer Subtraction:', sub)

num7 = 12
num8 = 4

mult = num7 * num8
print('Integer Multiplication:', mult)

num9 = 56
num10 = 12

div = num9 / num10
print('Division:', div)

num11 = -12.0
num12 = 4.9

print(type(num11))
print(type(num12))


int1 = 4.989
int2 = 5.190

rounded1 = round(int1)
print(rounded1) 

rounded2 = round(int2)
print(rounded2)


num = -12

value = abs(num)
print(value)

n1 = pow(2,3)
print(n1)

n2 = pow(2,3,5)
print(n2)

var = 5
var += 10
print(var)

greet = 'hello'
greet += ' word'
print(greet)

greet = 'guess who´s back'
greet *= 90
print(greet)

print(3 > 4)
print(3 < 4)
print(3 == 4)
print(4 == 4)
print(3 != 4)
print(3 >= 4)
print(3 <= 4)

age = int(input('Digite sua idade: '))

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >=13:
    print('You are a teeneger')
elif age >= 3:
    print('You are a young child')
else:
    print('You are not a adult yet')

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')
else:
    print('You are not eligible to vote')