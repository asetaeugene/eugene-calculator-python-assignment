#creating an empty list
my_list=[]
print(my_list)

#adding items to the list
my_list=[10, 20, 30, 40]
print(my_list)

#inserting value 15 at the second position
my_list.insert(1, 15)
print(my_list)

#second list
my_list2=[50, 60, 70]
print(my_list2)

#combining the two lists
my_list.extend(my_list2)
print(my_list)

#removing last item
my_list.remove(70)
print(my_list)

#sorting list in ascending order
my_list.sort()
print(my_list)

#finding and printing index value
index_of_30=my_list.index(30)
print(index_of_30)