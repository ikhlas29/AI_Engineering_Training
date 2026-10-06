#### Using map() function


def square(num):
    result =  num * 2
    return result
numbers=[1,2,3,4]
squared=list(map(square, numbers))  
# list() required as python return multiple "objects" from this function 
# loop through to compute the values into readable collection --> lazy function
print(squared)


#### Using filter() function

def is_odd(num):
    result = num % 2 != 0
    return result
numbers = [1,2,3,4,5,6,7,8,9]
odd_num=list(filter(is_odd, numbers)) 
# list() required as python return multiple "objects" from this function 
# loop through to compute the values into readable collection --> lazy function
print(odd_num)


#### Using reduce() function 

from functools import reduce
def multiplication(num1, num2):
    result = num1 * num2 
    return result
numbers=[1,2,3]
mul_result=reduce(multiplication, numbers) # no list() needed, as it return single value
print(mul_result)

