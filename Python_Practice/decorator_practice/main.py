# Create seperate function for the decorator instead of printing the decorator every time
def decorator_signs(given_function):
   def decorator_fun(*args, **kwargs):
    msg_iclude= "---------------------------\n"
    msg_iclude= msg_iclude + given_function(*args, **kwargs)
    msg_iclude= msg_iclude + "\n---------------------------"
    return msg_iclude
   return decorator_fun

#define the function -- to print required message
@decorator_signs    #Decorator function
def greeting_msg(pre_msg):
   return pre_msg + " This is Python Practice area!!"
print(greeting_msg("Salam,"))


#define the function -- to print required message
@decorator_signs   #Decorator function
def get_feedback(first_msg):
   return first_msg + "Seems usefull"
print(get_feedback("Feedback: "))

