#Write a Python program to find and print the first prime number greater than 100. Use a loop and the break statement to exit the loop once you find the prime number.
'''
for i in range(1,110):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2 and i>100:
        print(i)
        break'''
#Write a Python program to find and print the factors of a given number (input by the user). Use a loop and the break statement to exit the loop once you find all factors.
'''n=int(input())
for i in range(1,n+1):
    if n %i==0:
        print(i)
    if i==n:
        break'''
#Create a Python program that simulates a basic login system.
# Ask the user to enter a username and password.
# If the entered password is incorrect, give the user three attempts.
# Use the break statement to exit the loop if the password is correct or the user exceeds the maximum attempts.

'''corpass='123'
attempt=0
maxattempts=3
name=input("enter user name:")
password=input("enter password:")
for i in range(3):
    if password!=corpass and attempt<maxattempts:
        password=input("enter another password:")
        attempt+=1
        maxattempts-=attempt
    elif password==corpass or maxattempts>=3:
        print("you entered correct password or your max attemps completed")
        break'''
#Write a Python program that generates and prints the first 20 terms of the Fibonacci sequence.
# However, if a term is greater than 100,
# stop generating the sequence using the break statement.

a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(2,20):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    if c>100:
        break

