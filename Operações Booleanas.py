# Operações Booleanas

is_citizen = True
age = 17

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')
    else:
        print('You are not eligible to vote')

is_citizen = True
age = 25

print(is_citizen and age)

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')


age = 19
is_employed = False

print(age or is_employed)


age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount')
else: 
    print('You are not eligible for a student discount')

