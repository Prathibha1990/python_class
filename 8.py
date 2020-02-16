# # pir2+pilr+fgvgvg
# # radius=float(input('enter the value of radius'))
# # lenght=float(input('enter the value of length'))
# # print('cone area is',3.142*(radius**2)+3.142*lenght*radius)

# R,L=input('area of the radius and length').split()
# cone=float(3.142*R**2+3.142*L*R)
# print('area of the cone',cone)


###############

#format methods
a=3456.3456698
b=2.5438
c=456789.8
z=4567.1234567777
print('the value of {1} {2}'.format(a,b,c))

###########$

print('the value of {1:.3}'.format(a,b,c))
# the value of 2.54

print('the value of {1:.3f}'.format(a,b,c))
# the value of 2.544

print('the value of {3:.5f}'.format(a,b,c,z))
# the value of 4567.1

print(f'{b:3} {z:4f}')

print(f'{z:3} {c:4f}')




