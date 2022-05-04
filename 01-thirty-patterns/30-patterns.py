'''
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



# 8 Pyramid Pattern
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





# 9 hollow pyramid
print('\n Hollow Pyramid \n')

n=5
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        #print star at start and end
        if k==0 or k==2*i:
            print('*',end='')
        else:
            if i== n-1:
                print('*',end ='')
            else:
                print(' ',end='')
    print()









# 10 Reverse Pyramid
print('\n Reverse Pyramid \n')

for i in range(n):
    for j in range(i):
        print(' ',end='')
    for k in range(2*(n-i)-1):
        print('*',end='')
    print()


'''


#11 Dimond star pattern
n=5
print('\n Dimond \n')


for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()

for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(2*(n-i-1)-1):
        print('*',end='')
    print()


# 12 Hollow dimond
print('\n Hollow Dimond \n')

for i in range(n):
    for j in range(n-i-1):
        print(' ',end ='')
    for j in range(2*i+1):
        if j ==0 or j==2*i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
for i in range(n-1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(2*(n-i-1)-1):
        if j==0 or j==2*(n-i-1)-2:
            print('*',end='')
        else:
            print(' ',end='')
    print()




# 13 Hourglass

print(' \n Hourglass star pattern \n')


for i in range(n-1):
    for j in range(i):
        print(' ',end='')
    for k in range(2*(n-i)-1):
        print('*',end='')
    print()

for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()



# 14 Right Pascal Star pattern

print('')























































