### python program to count odd and even numbers in a list
list1 = [1,-2,5,2,3,7,-8,-9,15,17,-29]
negative_num = [x for x in list1 if x<0]
positive_num = [y for y in list1 if y>0]
print("The positvive numbers are",positive_num)
print("The negative numbers are",negative_num)
