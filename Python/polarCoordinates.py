# import cmath
# complexnumb = input()
# if "+" in complexnumb:
#     temp = complexnumb.split("+")
#     x = int(temp[0])
#     y= int(temp[1][0])
# elif "-" in complexnumb:
#     temp = complexnumb.split("-")
#     x = int(temp[0])
#     y= -(int(temp[1][0]))

# print(((x**2)+(y**2))**(1/2))
# print(cmath.phase(complex(x,y)))

import cmath;

num = complex(input())
z = complex(num)

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])