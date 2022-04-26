
#1 square pattern
print("Square Pattern")
for i in range(0,5):       #creating list of rows
    for j in range(0,5):   #create a list of colums
        print("*",end='')
    print()

print("\n")
for i in range(0,5):
    print("*"*5)     #printing * for 5 times and a newline







#2 hollow square
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



#3 Left triangle
print("\nleft triangle")
n=5
for i in range(1,n+1):
    #internal loop run for i times
    for k in range(1,i+1):
        print("*",end='')
    print()


for i in range(1,n+1):
    print("*"*i)





#4 right triangle
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







#5 Left downward triangle

print("\n left downward triangle \n")
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end='')
    print()


for i in range(n):
    print('*'*(n-i))







#6 right downward triangle

print('\n RIght Downward triangle \n')

n=5
for i in range(n):
    for j in range(i):
        print(" ",end='')
    for k in range(n-i):
        print('*',end='')
    print()




#7 Hollow triangle
print('\n Hollow Triangle \n')

n=6
for i in range(1,n+1):
    for j in range(i):
        #print star only at start and end of the row
        if j ==0 or j==i-1:
            print('*',end='')
        #print only star if its last row
        else:
            if i != n:
                print(' ', end='')
            else:
                print('*',end='')
    print()



#Pyramid Pattern
print('\n Pyramid Pattern \n')

n=5
for i in range(n):
    print(" "*(n-i-1)+'*'*(2*i+1))

print('\n')

for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()





#hollow pyramid
print('\n Hollow Pyramid \n')

























































