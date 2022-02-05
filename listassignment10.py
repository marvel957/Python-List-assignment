### python program to count odd and even numbers in a list
list1 = [1,4,5,2,3,7,8,9,15,17,29]
even_num = [x for x in list1 if x%2 ==0]
odd_num = [y for y in list1 if y%2 !=0]
print("The amount of even numbers is" , len(even_num),"and the number of odd numbers is" ,len(odd_num))
