#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    result = str[0:len(str)//2]
    return result
print (first_half("HiHi"))

##################################################
#Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

def first_two(str):
    if len(str) >2:
        return str[0:2]
    else:
        return str
print(first_two("Hello"))

#####################################################
#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sumnum(a,b):
    result = a+b
    if result>=10 and result<=19:
        return 20
    else:
        return result
print(sumnum(10,5))

#######################################################
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def two_array(a,b):
    new_list = [a[1] , b[1]]
    return new_list 
print(two_array([1,2,3],[4,5,6]))

###################################################3
# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotation(a):
 rotated_list = a[1:] + a[:1]
 return rotated_list
print(rotation([1,2,3]))

########################################################
#Practicing multiple args
def my_sum(*args):
    result = sum(args)
    return result
print(my_sum(1,2,3,5))