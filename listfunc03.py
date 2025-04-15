init_list = ["Anna", "Bob", "Cathy", "David", "Emily", "Fred", "Gary", "Helen", "Ivan", "Julia"]
second_list = ["Lemon", "Kevin"]
third_list = [1, 2, 7, 8, 5, 4, 4, 3, 2, 5]

# count
print(init_list.count("Bob"))
print(third_list.count(5))

# index
print(third_list.index(4))
# append
init_list.append("Somebody") # => ['Anna', 'Bob', 'Cathy', 'David', 'Emily', 'Fred', 'Gary', 'Helen', 'Ivan', 'Julia', 'Somebody']
print(init_list)
# init_list.append(second_list)
# print(init_list)

# extend
# A.extend(B) => 以 A 為主，把 B 內容加入
init_list.extend(second_list)
print(init_list)
# pop
idx = init_list.index("Helen")  # idx == 7
name1 = init_list.pop(idx)  # ['Anna', 'Bob', 'Cathy', 'David', 'Emily', 'Fred', 'Gary', 'Helen', 'Ivan', 'Julia']

init_list.pop()
init_list.pop()
init_list.pop()
init_list.pop()
print(init_list)

# # remove
print(third_list)
third_list.remove(5)
print(third_list)
# # clear
four_list = [3,3,4,4,5,5]
print(four_list)
third_list.clear()
print(four_list)
# sort
print(third_list)
third_list.sort()
print(third_list.sort())
print(third_list)
third_list.reverse()
print(third_list.reverse())
print(third_list)
