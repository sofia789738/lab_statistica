def triangle (a, b, c) :
    global t
    if (a*a-b*b-c*c)<0 and (-a*a+b*b-c*c)<0 and (-a*a-b*b+c*c)<0 :
        t = 'acute-angled'
    elif (a*a-b*b-c*c)>0 or (-a*a+b*b-c*c)>0 or (-a*a-b*b+c*c)>0 :
        t = 'obtuse-angled'
    elif (a*a-b*b-c*c)==0 or (-a*a+b*b-c*c)==0 or (-a*a-b*b+c*c)==0 :
        t = 'rectangular-angled'
    return t


a = float(input ('insert first side '))
b = float(input ('insert second side '))
c = float(input ('insert third side '))
print ('the triangle is ' + triangle(a, b, c))
