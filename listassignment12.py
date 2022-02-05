### python program to count even and odd numbers from a lis
list1 = [1,2,-5,8,-10,12,19,-21,-9,7,8,10]
negative_num = [x for x in list1 if x<0]
positive_num = [y for y in list1  if y>0]
count_positive = len(positive_num)
count_negative = len(negative_num)
print("The amount of positive number is ",count_positive)
print("The amount of negative number is ",count_negative)
