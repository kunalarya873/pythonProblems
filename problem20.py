# get 5 number from the user
# store in the array and display 
# find their sum 

import array as arr

a = arr.array('i',[])
s = 0
for i in range(5):#0 to 4 
    a.append(int(input("Enter a number to store in the array")))
for j in range(5):#0 to 4 
    print(a[j])
    s += a[j] # 2,3,4,5,6,7
print("Sum of the number is = "+str(s))