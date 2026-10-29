
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
    
