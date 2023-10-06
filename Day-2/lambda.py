from math import pi, sqrt
def fun (a, b, c):
    return a+b+c

print(fun(10, 20, 30))

fun_lambda = lambda a,b,c : a+b+c
print(fun_lambda(10, 20, 30))

circle_lambda = lambda r : (r**2*pi, 2*pi*r)
print(circle_lambda(3))

sim_int_lambda = lambda principle, rate, time_yrs : principle*rate*time_yrs/100
print(sim_int_lambda(100, 8, 1))

calculate_hypotaneous = lambda b, h : sqrt(b**2 + h**2)
print(calculate_hypotaneous(3,4))

convert_upper = lambda s : s.upper()
print(convert_upper("abCD"))

get_list = lambda a, b : list(range(a,b+1))
print(get_list(int(input("enter 1st no. \n")), int(input("enter 2nd no. \n"))))