
# FUNCTION BASICALLY USED TO CODE RESUABILITY



# factorial of a number


def fact(n):
    n_fact =1
    for i in range (1,n+1):
        n_fact=n_fact*1
    return n_fact
fact(4)





def function():
    print("hello raghav You in a function")
function()


#findout average no through function


def averagenumber(a,b):
    average=(a+b)/2
    print(average)
    return average
averagenumber(25,10)




#DOC STRING 

def my_function():
    """Demonstrates triple double quotes
    docstrings and does nothing really."""
   
    return None
  
print("Using __doc__:")
print(my_function.__doc__)
  
print("Using help:")
help(my_function)
