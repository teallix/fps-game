# Python zip function simple example

# Setting up lists 
prog_langs = ["python", "java", "c", "javascript"] 
tiobe_ranks = [1, 2, 3, 4]
features = [10, 20, 30, 40]

# Display input lists
print ("\nTest Input: **********\n Prog Langs : " + str(prog_langs)) 
print (" TIOBE Ranks : " + str(tiobe_ranks)) 
print (" Features : " + str(features)) 

# Using zip() to group values
zip_obj = zip(prog_langs, tiobe_ranks, features)

# printing zip object
print ("\nTest Result: **********\n Type of zip_obj is : ", type(zip_obj))

# convert zip object to a set 
final_res = set(zip_obj) 

# printing python zip result
print (" The final result after zip() : \n", final_res)