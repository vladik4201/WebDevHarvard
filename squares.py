from functions import square 

#importing from one module/file to another

for i in range(10):
    print(f"the square of {i} is {square(i)} ")

#you can also import the whole thing not just a variable or functions 
#from functions 
#for i in range(10):
#    print(f"the sqaure of {i} is {functions.square(i)})
#need to add a dot before the square to specify the import
