offices=['usa','brazil','europe','india','africa','canada','china']
for off in offices:
    print(off)
    if off=='europe':
        print('office in ',off)
    elif off=='india':
        print('office in',off)
    else:
        print('not specifed in this list')
print('.............................')
companies=['usa','brazil','europe','india','africa','canada','china']
for company in companies[:3]:
    print(company)
    
college=['ksou','kuvempu','vtu','sahyadri']
for degree in college:
    if degree=='sahyadri':
        print('graduation in ',degree)
    elif degree=='kuvempu':
        print('graduation in',degree)
    else:
        print('not entered the schools')
