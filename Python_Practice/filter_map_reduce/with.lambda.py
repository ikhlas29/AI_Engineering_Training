#lambda function is a small and anonymous function in Python, defined using the "lambda" keyword 
# rather than the def statement

#### Using map() function with lambda

numbers=[1,2,3,4]
squared=list(map(lambda num: num * 2, numbers)) 
print(squared)

#### Using filter() function with lambda

numbers=[1,2,3,4,5,6,7]
odd_num=list(filter(lambda num: num % 2 !=0, numbers))
print(odd_num)

#### Using reduce() function with lambda

from functools import reduce
numbers=[1,2,3,4]
sum_num=reduce(lambda num1, num2: num1 + num2, numbers)
print(sum_num)

