def fun_calculator(x, y, z):
    if y == '+':
        return x+z
    elif y == '-':
        return x-z
    elif y == '/':
        return x/z
    elif y == '*':
        return x*z
    elif y == '%':
        return x % z
    elif y == '^':
        return x**z
    else:
        return "Error:"


f_n = int(input("Enter the First number..."))
c_operator = input("Enter the operator ...")
s_n = int(input("Enter the Second number..."))
print(fun_calculator(f_n, c_operator, s_n))
