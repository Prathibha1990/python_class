a=int(input('enter the value of a'))
b=int(input('enter the value of b'))
c=int(input('enter the value of c'))

if a>b and a>c:
    print('a is grater than')
elif b>c and b>a:
    print('b is grater than')
elif c>a and c>b:
    print('c is grater than')
    
else:
    print('wrong')
