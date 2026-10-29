'''
pattern-1
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()
'''
'''
pattern-2
* 
* * 
* * * 
* * * * 
* * * * * 
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()
'''
'''
pattern-3

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

n=int(input())
for i in range(1,n+1):
    for k in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
'''
'''
pattern-4
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * * 

n=int(input())
for i in range(1,n+1):
    for k in range(n-i):
        print(' ',end=' ')
    for j in range(2*i-1):
        print('*', end=' ')
    print()
'''
'''
pattern-5

A B C 
D E F 
G H I 

n=int(input())
c=65
for i in  range(1,n+1):
    for j in range(1,n+1):
        print(chr(c),end=' ')
        c+=1
    print()
'''
'''
pattern-6

A B C 
A B C 
A B C 

n=int(input())
for i in range(1,n+1):
    c=65
    for j in range(1,n+1):
        print(chr(c),end=' ')
        c+=1
    print()'''
'''
pattern-7

A A A 
B B B 
C C C 

c=65
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(c),end=' ')
    c+=1
    print()'''

'''
pattern-8 

* * * 
  * * 
    * 

r=int(input())
num=3
s=3
for i in range(1,r+1):
    for k in range(r-num):
        print(' ',end=' ')
    num-=1
    for j in range(s):
        print('*',end=' ')
    s-=1
    print()
    
r=int(input())
for i in range(r,0,-1):
    for k in range(r-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
'''
'''
pattern-9

* * * 
* * 
* 
r=int(input())
for i in range(r,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
'''
r=5
c=7
for i in range(r):
    for j in range(c):
        if i==0 and j==c//2 or i==r-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
