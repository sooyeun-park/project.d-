#! /usr/bin/env python
l_test1 = [1,2,3, 'apple', ' ']
l_test2 = ['a','b', 'c']
print(l_test1 + l_test2)
print('-' *30)

numbers=[1,2,3]
print("numbers[1]:", numbers[1])
print("numbers[-1]:", numbers[-1])
print("numbers[::-1]:", numbers[::-1])
print('-' * 30)
print('-' *30)

numbers_ex = [1,2,3,4,5,6,7,8,9,0]
print("numbers_ex[0:5:1]:" , numbers_ex[0:5:1])
print("numbers_ex[0::1]:" , numbers_ex[0::1])
print("numbers_ex[::-1]:" , numbers_ex[::-1])
print('-' *30)

l_num = [0,1,2,3]
print(l_num)
l_num.append([5,6,7])
print(l_num)
l_num.extend([88])
print(l_num)
print('-' *30)

d_dict = {'a_str':'Apple!', 'b_list':[1,2,3,4], 'c_tuple':('a','b', 'c'), 'e_dict':{1:'one', 2:'two'}}
print('d_dict', d_dict)
print ('d_dicta', d_dict['b_list'])
print ('d_dicta', d_dict['b_list'][0]) 
print ('d_dicta', d_dict['b_list'][1])
print('-' *30)

setA = {2,3,6,5,7,2,31}
setB = {3,5,23,6}
print(setA | setB)
print(setA & setB)
print(setA - setB)
print(setA ^ setB)
setA.add(120)
print(setA)
print(set.union(setA, setB))
print( setA | setB )
print('-' *30)

print(bool(0))
print(bool(1))
print('-' *30)

myVar1 = input('var1: ')
if myVar1 == '1':
    print('myVar1 is 1!')
else :
    pass
    #print('var1 is not 1!')
print("Good Bye!")

print('-' *30)
i= 0
while True :
    i = i+1 #i += 1
    print('*'* i ) 
    if i > 30 : 
        break
print('-' *30)

for i in [1,2,3]:
    print(i)
print("done!")
print('-' *30)

l_range = [1,2,5,3,1,7]
a = "*"
for i in l_range:
    print('current number: ',i)
    if i == 1 :
        print(i)
    else :    
        continue
print("done!")
print('-' *30)

totalSum = 0
for i in range(3):
    totalSum += i
    print(i)
print('totalSum:', totalSum)
print('-' *30)

ipnum = input('number: ')
while not ipnum.isdigit():
    ipnum = input('number is not digit. please reinput the number :')    
ipnum=int(ipnum)

#while if  ipnum > 19 : 
#    print('number is too big')
#    continue    
#elif ipnum < 2 : 
#    print('number is too small')
#    continue
#else :  
#    for i in range(1,10,1):
#        print(ipnum * i)
#        break
#print('-' *30)

#def showHello():
#    print('Hello!')
#    return '1'
#a = showHello()
#print('number?')
#print(a)
print('-' *30)

#def book_0(name, age, book1, book2):
#    print('name:{0}, age:{1}'.format(name, age), end = ' ')
#    print('book:', book1, book2)

#def book_1(name, age, *books):
#    print('name: {0}, age: {1}'.format(name, age), end = ' ')
#    print('book:', end = ' ')
#    for book in books:
#        print(book, end = " ")
#    print()
#book_0('yune', 5, 'python', 'basic')
#book_1('yune', 5, 'python', 'basic')
#book_1('yune', 5, 'python', 'basic', 'photo')
 print('-' *30)

print('lambda:',(lambda a,b:a+b)(3,4))

