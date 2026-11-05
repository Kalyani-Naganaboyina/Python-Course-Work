
#sum of prime digits in a number
'''n=1234567
s=0
while n!=0:
    r=n%10
    fc=0
    for i in range(1,r+1):
        if r%i==0:
            fc+=1
    if fc==2:
        s+=r
    n=n//10
print(s)'''

#sum of odd digits in a number

'''n=12345
s=0
while n!=0:
    r=n%10
    if r%2==1:
        s+=r
    n=n//10
print(s)
'''
#Reverse a number using a while loop
'''n=int(input())
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
    '''
 # palindrome or not
'''n=int(input())
temp=n
rev=0
while temp!=0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if n == rev:
    print("palindrome")
else:
    print("not a palindrome")'''

#Armstrong or not
'''n=int(input())
s=str(n)
temp=n
t=0
d=len(s)
while temp>0:
    r=temp%10
    t+=(r**d)
    temp//=10
if n == t:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")'''

#Strong number
'''n=145
copy=n
s=0
while n!=0:
    d=n%10
    fact=1
    i=1
    while i<=d:
        fact=fact*i
        i+=1
    s+=fact
    n=n//10
if copy==s:
    print("strong number")
else:
    print("not a strong number")'''

#neon number
'''n=9
t=0
s=n**2
while s>0:
    d=s%10
    t+=d
    s//=10
if n==t:
    print("Neon number")
else:
    print("not a neon number")'''

#happy number
'''n=7
m=n
while m!=1 and m!=4:
    t=0
    while m>0:
        d = m % 10
        s = d * d
        t += s
        m //= 10
    m=t
if m==1:
    print("Happy number")
else:
    print("Not a happy number")
'''
#Spy number
'''n=1124
ss=0
ps=1
while n!=0:
    d=n%10
    ss+=d
    ps*=d
    n=n//10
if ss==ps:
    print("SPY number")
else:
    print("Not a SPY number")
'''
#automorphic
'''n=int(input())
temp=n
s=n*n
flag=True
while temp>0:
    if temp%10 != s%10:
        flag=False
        break
    temp=temp//10
    s=s//10
print("Automorphic" if flag else "Not a automorphic number")'''

#trimorphic
'''n=int(input())
temp=n
c=n**3
flag=True
while temp>0:
    if temp%10 != c%10:
        flag=False
        break
    temp=temp//10
    c=c//10
print("Trimorphic" if flag else "Not a Trimorphic number")'''


