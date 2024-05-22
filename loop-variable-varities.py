Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

numbers = list(range(12))
numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# print all the even numbers
for everynum in numbers:
    if everynum%2 == 0:
        print(everynum)

        
0
2
4
6
8
10
# add all the numbers to a list called even


even=[]
for everynum in numbers:
    if everynum%2 == 0:
        even.append(everynum)

        
even
[0, 2, 4, 6, 8, 10]


# sum of all the even nums above

total=0

for everynum in numbers:
    if everynum%2 == 0:
        total=total+everynum

        
total
30


t='0'
for everynum in numbers:
    if everynum%2 == 0:
        t=t+str(everynum)

        
t
'00246810'
t='0'
for everynum in numbers:
    if everynum%2 == 0:
        t=t+str(everynum)
        print(t)

        
00
002
0024
00246
002468
00246810



# sum of all the first 100 even natural numbers

range(1,101)
range(1, 101)

summ=0
for every_num in range(1,101):
    if every_num%2 == 0:
        summ=summ+every_num

        
summ
2550


sum_even=0
sum_odd=0

for every_num in range(1,101):
    if every_num%2 == 0:
        sum_even=sum_even+every_num
    else:
        sum_odd=sum_odd+every_num

        
sum_even
2550
sum_odd
2500



numb={}
numb
{}
del numb


n={}
n
{}
n['even']=[]
n
{'even': []}
n['odd']=[]
n
{'even': [], 'odd': []}


for every_num in range(1,101):
    if every_num%2 == 0:
       n['even'].append(every_num)
    else:
        n['odd'].append(every_num)

        
n
{'even': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100], 'odd': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]}

n['eve']
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    n['eve']
KeyError: 'eve'
n['even']
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
n['odd']
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]



# membership operator
# to check membership of a value

numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

6 in numbers
True


's' in 'sreedhar'
True

's' in 'Sreedhar'
False




"this is a beautiful morning"
'this is a beautiful morning'

"this is a beautiful morning".split(" ")
['this', 'is', 'a', 'beautiful', 'morning']



"this is a beautiful morning".split(" ")[3]
'beautiful'



"albert eistein".split(" ")
['albert', 'eistein']

>>> "albert eistein".split(" ")[0]
'albert'
>>> 
>>> "albert eistein".split(" ")[1]
'eistein'
>>> 
>>> "albert eistein".split(" ")[0].title()
'Albert'
>>> 
>>> "albert eistein".split(" ")[1].title()
'Eistein'
>>> 
>>> "Mr."+ albert eistein".split(" ")[1].title()
SyntaxError: unterminated string literal (detected at line 1)
>>> "Mr."+ "albert eistein".split(" ")[1].title()
'Mr.Eistein'
>>> 
>>> 
