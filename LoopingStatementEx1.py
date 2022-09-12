#Printing Even or Odd numbers between 1 and 21

a=input('Enter Odd or Even :').upper()
for i in range(1,21):
    if a=='EVEN' and i%2==0:
        print(i)
    elif a=='ODD' and i%2!=0:
        print(i)
