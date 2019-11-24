
my_list = [3,4,3,'helooe',True, ['a',4,5]] # can hold differnt types

size = len(my_list)
my_list.append("new item")
my_list.extend([9,40,3,4])
remove_last = my_list.pop()
remove_any = my_list.pop(4)
index_neasted = my_list[5][0]

# list comprehension

matrix = [[1,2,3], [4,5,6], [7,8,9]]
firt_column = [row[0] for row in matrix]
second_column = [row[1] for row in matrix]

print(second_column)
