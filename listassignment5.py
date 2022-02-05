# python program to find the sum and average of a list
original_list =[2,5,6,8,9,10,45]
f = len(original_list)
initial = 0
for i in original_list:
    initial += i
sum_of = initial
average = initial/f
print("The sum of the elements is",sum_of," The average is",average)
