# Python zip function
# Zip two or more lists of different sizes

# Setting up lists 
in_list1 = [11, 21, 34, 12, 31] 
in_list2 = [23, 25, 54, 24, 20, 27] 
in_list3 = [23, 25, 54, 24] 

# Display input lists 
print ("\nTest Input: **********\n Input List (1) : " + str(in_list1)) 
print (" Input List (2) : " + str(in_list2)) 
print (" Input List (3) : " + str(in_list3)) 

# Find the smallest list to iterate
size_smallest_list = min(len(in_list1), len(in_list2), len(in_list3))

# Call the zip function on input lists of different sizes
out = zip(in_list1, in_list2, in_list3)

# Convert zip object to a list
result_set = list(out)

# printing zip() result
print ("\nTest Result: **********\n Size of the smallest list is : ", size_smallest_list) 
print (" Size of the zipped resultant list is : ", len(result_set))
print (" Zipped resultant list is : \n", result_set)