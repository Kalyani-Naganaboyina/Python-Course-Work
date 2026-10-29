#Print numbers from 1 to 5 using a for loop
'''for i in range(1,6):
    print(i)'''
#Print all characters of a string
'''s=input()
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c+=1
        print(i)
print(c)
for j in s:
    if j not in v:
        print(j)'''
#Find sum of digits of a number
'''n=int(input())
s=str(n)
t=0
for i in s:
    t+=int(i)
print(t)'''

#Print multiplication table of a number
'''n=int(input())
for i in range(1,11):
    print(f"{n}* {i} = {n*i}")'''

#Print factorial of a number
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)'''

#Print squares of numbers from 1 to n
'''n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i*i)
print(l)'''

#Print a countdown from a given number using a for loop.
'''n=int(input())
for i in range(n,0,-1):
    print(i)'''
    
#fibanocci series
''''n=int(input())
a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i  in range(2,n):
    c=a+b
    a=b
    b=c
    print(c, end=' ')'''

#find factors of a given number
'''n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
'''
#perfect number or not
'''n=int(input())
s=0 
for i in range(1,n):
    if n%i==0:
        s+=i
if n==s:
    print("perfect number")
else:
    print("not a perfect number")'''

#check whether given number is palprime or not

'''n=int(input())
temp=n
fc=0
rev=0
fact=1
while temp!=0:
    rem=temp%10
    rev=rev*10+rem
    temp//=10
for i in range(1,n+1):
    if n%i==0:
        fc+=1
if n== rev and fc==2:
    print("palprime")
else:
    print("not a palprime")'''
    