Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> s = {}
>>> 
>>> type(s)
<class 'dict'>
>>> 
>>> s = {1,1,1,1,1,1,1,1111,2,2,4,3,5,9,6,7,7,7,7,7777}
>>> s
{7777, 2, 3, 1, 4, 5, 6, 7, 9, 1111}
>>> 
>>> s.add(1)
>>> s
{7777, 2, 3, 1, 4, 5, 6, 7, 9, 1111}
>>> s.add(11)
>>> s
{7777, 2, 3, 1, 4, 5, 6, 7, 9, 11, 1111}
>>> 
>>> 
>>> weekdays = ['sun','mon','tues','wednes','thurs','fri','sat']

weekdays
['sun', 'mon', 'tues', 'wednes', 'thurs', 'fri', 'sat']
weekends = ['sun','sat']
weekends
['sun', 'sat']

type(weekends)
<class 'list'>

set(weekdays)
{'fri', 'thurs', 'wednes', 'tues', 'sun', 'sat', 'mon'}
weekdays=set(weekdays)
weekends = set(weekends)
weekends
{'sat', 'sun'}


weekends.union(weekdays)
{'fri', 'thurs', 'wednes', 'tues', 'sun', 'sat', 'mon'}


odd = {3,5,7,9,11}
even = {2,4,6,8,10}
odd
{3, 5, 7, 9, 11}
even
{2, 4, 6, 8, 10}

odd.union(even)
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
odd = {3,5,7,9,11,1111}
even = {2,4,6,8,10,1111}

odd.intersection(even)
{1111}


odd
{3, 5, 1111, 7, 9, 11}
even
{2, 4, 6, 1111, 8, 10}


odd.difference(even)
{3, 5, 7, 9, 11}

even.difference(odd)
{2, 4, 6, 8, 10}


odd | even
{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1111}

odd & even
{1111}
