#Alphabet Patterns in Python

#print A-Z

#Capital letters ___65 in char is A  90 in Char is Z

for i in range(65,91):
    print(chr(i), end=' ')
print('\n')

#Small Letters ___97 in chr is a  and 122 in chr is z
for i in range(97,123):
    print(chr(i), end=' ')





#Square pattern
print('\n Square pattern 1\n')
#1
n=5
count = 0
for i in range(5):
    for j in range(5):
        print(chr(65+ count),end=' ')
        #changing charecters
        count += 1
    print()
        
#2
print('\n Square Pattern 2 \n')

for i in range(5):
    for j in range(5):
        print(chr(65+i),end=' ')
    print()


#3
print('\n Square Pattern 3 \n')

for i in range(5):
    for j in range(5):
        print(chr(65+j),end=' ')
    print()



# 2 Left triangle
print('\n Left Triangle \n')
for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end ='')
    print()
        


# 3 Right Triangle pattern
print('\n Right triangle pattern \n')
n=5
for i in range(n):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print(chr(65+j),end ='')
    print()
        


# 4 Hollow triangle alphabet pattern
























