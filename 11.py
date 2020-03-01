# tuple()
# non mutable type()
# tuples are faster compaired to list


x=(100,'lohit')
print(x)

print(type(x))


xyz=30,30.445j,'name','school'
print(xyz)
print(type(xyz))

empty_tuple=()
print(empty_tuple)

tuple1=(100,200,300)
tuple2=(100,200,300)
print(tuple1+tuple2) #it can't chanege original value

print(sum(tuple1+tuple2))

# length function
tuple10=('java','php','python','sql')
print(len(tuple10))

tuples=('john','mary','school',42556,4356,)
print(tuples[1])

# tuples[2]='lohith'
# print(tuples) #TypeError: 'tuple' object does not support item assignment

#tuple slicing()
tuples1=('john','mary','school',42556,4356,('lohit'))

print(tuples1[::-1])

print(tuples1[::2])

print('####################')


my_new_tuple=('a','b','c','d','e')

print('a' in my_new_tuple)

print('a' not in my_new_tuple)

# maximum & minimum function

list=[1,2,3,4,5,6,7,89]

print(max(list))
print(min(list))

# index function

list=[1,2,3,'prathi',5,6,7,89]
print(list.index('prathi'))

print('####################')


# count function()
list4=['prathibha','prathibha',1,3,2]
print('this counts prathibha',list4.count('prathibha'))




