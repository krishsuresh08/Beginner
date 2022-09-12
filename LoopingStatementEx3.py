#Printing a Pattern
#Expected output
'''
1
2 3
4 5 6
7 8 9 10
'''
n=0
for i in range(1,5): 
    for j in range(1,i+1):
        n+=1
        print(n,end=' ')
    print()
