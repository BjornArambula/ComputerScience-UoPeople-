#Example 1
def show_message(message): #Function with message var passed through
    print(message)
    
show_message("My name is Bjorn") 

#Example 2
variable = 2 + 2 
show_message(10)
show_message(variable)
show_message("var" + "iable")

#Example 3
def local_var_example():
    localvar = "Local Variable"
    print(localvar, "only works within the local_var_example() function")
    
local_var_example() #Will print the variable and string. 

#Example 4
def show_temp(temperature):
    print("The temperature is", temperature)
show_temp(54) #Current temp is 54
    
#Example 5
name = "Bjorn"

def var_outside():
    name = "David"
    print("My name is", name) #will print David since the variable is inside the function
var_outside()
print(name) #Will print Bjorn since the var is outside the function

