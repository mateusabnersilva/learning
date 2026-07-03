def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()


my_var = 100

def show_var():
    print(my_var)

show_var()
print(my_var)


var1= 7

def show_vars():
    global var2
    var2 = 10
    print(var1)
    print(var2)

show_vars() 
print(var2)


num = 10

def change_num():
    global num
    num = 20

change_num()

print(num)
