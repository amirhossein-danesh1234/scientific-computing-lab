import numpy as np

# goel : solving the ax^2 + bx + c = 0 
# With a = 10^-4, b=-10^4, c=10^-4
print("please enter the value of a, b, c\nax^2 + bx + c = 0\n")

a = np.float64(input("a : "))
b = np.float64(input("b : "))
c = np.float64(input("c : "))
# use float64 for better accuracy

D2 = b**2 - 4*a*c
if D2 > 0:
    D = np.sqrt(D2)

    # for calculate accuracy we calculate :
    # if   b<0 : x1 = -(b + D)/2a
    # else b>0 : x1 = (-b + D)/2a
    # then we calculate x2 from x2*x1 = c/a ---> x2 = c/(a*x1)


    if b < 0 :
        x1 = (-b + D)/(2 * a)
    else:
        x1 = -(b + D)/(2 * a)

    x2 = c/(a*x1)
    if x1 > 0:
        x11 = f" - {x1}"
    elif x1 == 0:
        x11 = ""
    else:
        x11 = f" + {-x1}"

    if x2 > 0:
        x22 = f" - {x2}"
    elif x1 == 0:
        x22 = ""
    else:
        x22 = f" + {-x2}"
    print(f"\nx1 = {x1}\nx2 = {x2}")
    print(f"\n({a})x^2 + ({b})x + ({c}) = (x{x11})(x{x22})")

elif D2 == 0:
    x = -b/(2*a)
    if x > 0:
        xx = f" - {x}"
    elif x == 0:
        xx = ""
    else:
        xx = f" + {-x}"
    print(f"\nx1 = x2 = {x}")
    print(f"\n({a})x^2 + ({b})x + ({c}) = (x{xx})(x{xx})")

elif D2 < 0:
    print("Delta is complex number")
    
"""
output : 

please enter the value of a, b, c
ax^2 + bx + c = 0

a : 0.0001
b : -10000
c : 0.0001

x1 = 100000000.0
x2 = 1e-08

(0.0001)x^2 + (-10000.0)x + (0.0001) = (x - 100000000.0)(x - 1e-08)
"""