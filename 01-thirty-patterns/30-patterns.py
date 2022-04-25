
##square pattern
print("Square Pattern")
for i in range(0,5):       #creating list of rows
    for j in range(0,5):   #create a list of colums
        print("*",end='')
    print()

print("\n")
for i in range(0,5):
    print("*"*5)     #printing * for 5 times and a newline







##hollow square
print("Hollow Square")
size=5
for i in range(size):
    for j in range(size):
        #printing * compleately in first and last row
        #printing * only in first and last positon in other rows
        if i ==0 or i==size-1 or j==0 or j==size-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print("\n")
for i in range(size):
    #print star in first and last row
    if i==0 or i==size-1 :
        print('*'*size)
    else:
        #print star in first and last positon in other rows
        print('*'+" "*(size-2)+'*')



##Left triangle
print("\nleft triangle")
n=5
for i in range(1,n+1):
    #internal loop run for i times
    for k in range(1,i+1):
        print("*",end='')
    print()


for i in range(1,n+1):
    print("*"*i)





##right triangle
print("\n Right Triangle \n")
size = 5
for i in range(size):
    for j in range(1,size-i):
        print(" ",end='')
    for k in range(0,i+1):
        print("*", end='')
    print()

for i in range(1,size+1):
    print(" "*(size-i)+'*'*i)







##Left downward triangle

print("\n left downward triangle \n")
































