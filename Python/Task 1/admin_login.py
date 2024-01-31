import maskpass


# function askpass is using this both parameter as by default prompt="Enter admin password : ",mask='*'
def fun2():
    pwd = maskpass.askpass()
    if pwd == 'Admin@123':
        print("Access Granted")
    else:
        print("Invalid password")
        fun2()

def fun1():
    uname = (input("Enter admin username : "))
    if uname =='admin':
        fun2()
    else:
        print("Invalid username")
        fun1()

fun1()