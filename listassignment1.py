# python program to interchange the first and last element of a list
original_list = [1,2,3,4,5,6,7,8,9,10]
#print the old list
print("Your Original list is : ",original_list)
#declare a and b to store first and last element respectively.

a = original_list[0]
b = original_list[-1]
original_list[0] = b
original_list[-1] = a
print("Your new list is : ",original_list)
