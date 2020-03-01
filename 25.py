# items1=['orange','banana','mango','kiwi',123,45,'apple','water melon']
# for fruites in items1:
#     print(fruites)
#     if fruites=='mango':
#         print('fruite is',fruites)
#     elif fruites==123:
#         print('its not a fruite ',fruites)
#     else:
#         print('none of these')
# print('..........................')



items1=['orange','banana','mango','kiwi',123,45,'apple','water melon']
for abc in items1[-1:]:
    print(abc)

# program to check if a number is prime or not num = 407
num=int(input('enter the number is'))
if num>1:
    for i in range(2,num//2):
        if(num%i)==0:
            print('num is a prime',num)
    else:
        print('number is not prime no',num)
    