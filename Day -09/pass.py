#Create a Python program that iterates over a list of integers and prints all even numbers.
# For odd numbers, use the pass statement to do nothing.
'''l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(i,end=' ')
    else:
        pass'''

#Write a Python program that asks the user to input a list of numbers. For each number in the list,
# check if it's a prime number. If it's prime, print it; if not, use the pass statement.
'''l=list(map(int,input().split()))
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i,end=' ')
    else:
        pass'''
#Implement a Python program that simulates a basic class structure for a geometric shape.
# Create a class named Shape, and for now,
# use the pass statement to indicate that further methods need to be added in the future.
'''
class Shape:
    pass
s=Shape()
'''
#Create a Python program to check if a given number is a perfect square.
# If it is, print a message; otherwise, use the pass statement.
'''n=int(input())
if n==(n*n)/n:
    print("Perfect Square")
else:
    pass'''

#Write a Python program to iterate through a list of sentences and
# check if each sentence ends with a question mark.
# If it does, print the sentence; otherwise, use the pass statement.

l=["who are you?","what is this?","i am ok."]
for s in l:
    if s[-1]=='?':
        print(s, end=' ')
    else:
        pass