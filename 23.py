# slicing in for loop
offices=('info',35,'sysco',45,'hp','inno','base')
for office in offices[3:]:
    print(office)

# for loop in if condition
print('---------------------')
for office in offices:
    if office=='sysco':
        print('name is ', office)
    elif office=='hp':
        print('name is ', office)
    else:
        print('nothing', office)

