rows = int(input("Enter the number of rows : "))

for i in range(rows):
    for j in range(0,i+1):
        print('*',end='')
    print()
for i in range(1,rows):
    for j in range(i,rows):
        print('*',end='')
    print()
