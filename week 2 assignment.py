#1.empty list
my_list = []
#2. Append elements to the list 
my_list.append(10) 
my_list.append(20) 
my_list.append(30)
my_list.append(40)
 # Print the updated list
print(my_list)
#3. Insert value 15 at the second position  
my_list.insert(1, 15) 
# Print 
print(my_list)
#4. Extend the list with another list
my_list.extend([50, 60, 70]) 
# Print
print(my_list)
#5. Remove the last element 
my_list.pop() 
# Print the updated list 
print(my_list)
#6. Sort the list in ascending order 
my_list.sort() 
print(my_list)
#7. Find the index of the value 30 
index_of_30 = my_list.index(30) 
# Print the index print
print(index_of_30)