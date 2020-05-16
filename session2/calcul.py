a = input('a ')
b = input('b ')
c = input('c ')
delta = int(b)**2 - 4*int(a)*int(c)
n = - int(b) / 2 / int(a)
m1 = (-int(b) + int(delta)**0.5) / 2 / int(a)
m2 = (-int(b) - int(delta)**0.5) / 2 / int(a)


if delta < 0:
    print('phuong trinh vo nghiem')
elif delta == 0:
    print(n)
else:
    print(m1)
    print(m2)
