#Create a Python program to calculate the sum of all numbers from 1 to 100.
# However, if the number is divisible by both 3 and 5, skip it using the continue statement.
'''s=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    else:
        s+=i

print(s)'''

#Implement a program that calculates the average of a list of numbers,
# but ignore any negative numbers.
# Use the continue statement to skip negative numbers in the list.
'''l=list(map(int,input().split()))
n=len(l)
for i in l:
    a=i/n
    if a<0:
        continue
    else:
        print(a,end=' ')'''
#Write a Python program that finds the first 10 even numbers.
# If a number is divisible by 3, skip it using the continue statement.

'''for i in range(2,10):
    if i%2==0:
        if i %3==0:
            continue
        else:
            print(i,end=' ')'''
#Implement a Python program that counts and
# prints the number of vowels in a given string.
# Use a loop to iterate through the characters in the string and
# use the continue statement to skip consonants.

'''c=0
s=input()
v="AEIOUaeiou"
for i in s:
    if i in v:
        c+=1
    else:
        continue
print(c)'''

#at least 8 characters long, keep asking for a valid password using a loop.
# Use the continue statement to skip further processing until a valid password is provided.
'''while True:
    password=input("enter password: ")
    if len(password)<8:
        continue
    else:
        print("Valid password")
        break'''

#Write a Python program to find the sum of all even numbers from 1 to 100.
# However, if a multiple of 7 is encountered, skip it using the continue statement.
for i in range(1,101):
    if i%2==0:
        if i%7==0:
            continue
        else:
            print(i,end=' ')