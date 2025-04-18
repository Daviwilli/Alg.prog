def g0(x0, x1, i=1):
    return f'(y{i}-y{i-1})/'+str(x1-x0)

def a(x0,x1,x2):
    a = (x2 - x1)(x1-x0)(x2-x0)
    return a

def gi(x0,x1,x2, i):
    v1 = (-1*((x2-x1)**2))/a(x0,x1,x2)
    v2 = (((x2-x1)*2)-((x1-x0)*2))/a(x0,x1,x2)
    v3 = ((x1-x0)**2)/a(x0,x1,x2)/a(x0,x1,x2)
    return f'({str(v1)})y{i-1}'+' + '+f'({str(v2)})y{i}'+' + '+f'({str(v3)})y{i+1}'

print('g0 = ', g0(1,6))
print('g1 = ', gi(1,6,8,1))
print('g2 = ', gi(6,8,9,2))
print('g3 = ', g0(8,9,3))