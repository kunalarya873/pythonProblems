# to generate num 1 to 10
# find their square, cube, and addition of square and cube

print("Number\t\t Square\t\t Cube\t\t Addition")
for i in range(1,11):  
    print(str(i)+"\t\t"+str(i*i)+"\t\t"+str(i*i*i)+"\t\t"+str((i*i)+(i*i*i)))