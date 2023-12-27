fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

init_tuple = ()
print (init_tuple.__len__())

init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')
 
print(init_tuple_a == init_tuple_b)

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')
 
print (init_tuple_a + init_tuple_b)

init_tuple_a = 1, 2
init_tuple_b = (3, 4)
 
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)