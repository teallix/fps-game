from ctypes import *

so_file = "allfiles/c++/Teallix/c++inpython/cfunctions.c++"

my_functions = CDLL(so_file)

print(type(my_functions))
print(my_functions.square(10))

print("Done")