#Check if a given number is a multiple of 5 or not.
'''n=25
if n%5==0:
    print(f"{n} is a multiple of 5")
else:
    print(f"{n} is not a multiple of 5")'''


#Take an input number and check whether it is a three-digit number.(if-else)
'''n=int(input())
n=str(n)
if len(n)==3:
    print(f"{n} three digit num")
else:
    print(f"{n} not a three digit num")''' 
    
    
#Take a character input and check if it is a vowel or consonant.
'''s=input()
v='AEIOUaeiou'
if s in v:
    print(f"{s} is a vowel.")
else:
    print(f"{s} is consonant.")'''
    
# Ask the user to enter their name. If the name is “admin”, print “Welcome, Admin!”
'''s=input()
if s =='admin':
    print("Welcome, Admin!")
'''
 #Take an input number and check whether it is a three-digit number.(if-else)
'''n=int(input())
if 100 <= abs(n) <=999:
     print(f"{n} is a three digit number.")
else:
    print(f"{n} is not a three digit number.")
'''
#Take a character input and check whether it is uppercase letter or lowercase letter or not letter.
'''s=input()
if s.isupper():
    print("upper letter")
elif s.islower():
    print(" lower letter")
else:
    print("not a letter")'''
    
#Determine if a given number is a perfect square.
'''n=int(input())
if n>=0 and int(round(n**(1/2))**2)==n:
    print("perfect square ")
else:
    print("not a perfect square ")'''
    
#Determine if a number is a perfect cube.
'''n=int(input())
if n>=0 and int(round(n**(1/3))**3)==n:
    print("perfect cube")
else:
    print("not a perfect cube")
    '''
    
# palindrome or not
'''s=input()
if s== s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")'''

#check perfect square or not
n=int(input())
s=int(round((n**(1/2))**2))
if n==s:
    print("perfect square")