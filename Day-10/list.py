#find unquie elements in a list
'''l=list(map(int,input().split()))
nl=[]
for i in l:
    if i not in nl:
        nl.append(i)
print(nl)'''

#print duplicate elements in a list

'''l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print(l[i],end=' ')'''
'''l=[]
for _ in range(4):
    a=int(input("enter value:"))
    l.append(a)
print(l)
'''

#product of smallest number and second largest number from the list
'''n=int(input())
l=list(map(int,input().split()))[:n]
max=l[0]
second=0
s=l[0]
for i in l:
    if i>max:
        second=max
        max=i
    elif i>second and i!=max:
        second=i
    if i<s:
        s=i
print(second*s)'''

#Reverse a list in Python
'''l=list(map(int,input().split()))
for i in range(len(l)-1,-1,-1):
    print(l[i],end=' ')'''

#Remove duplicates from a list in Python ?
'''l=[2,2,3,4,5,1,5]
print(list(set(l)))'''
#remove duplicates and print sum of odd elements in the list

'''l=[2,2,3,1,4,3,5]
for i in l:
    if l.count(i)>1:
        l.remove(i)
print(l)
s=0
for i in l:
    if i%2==1:
        s+=i
print(s)
'''

#Sort a list in ascending and descending order ?
'''
l=[2,5,6,7,3,4,1]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

'''
#Check if a list is empty in Python
'''
l=[]
print("empty list" if l==list() else "not empty list")

'''
#Find the index of a specific element in a list
'''
l=[2,4,5,6,7]
print(l.index(6))
'''
#Count the occurrences of an element in a list ?
'''
l=[1,2,2,3,1,5]
print(l.count(2))'''

#Merge two lists in Python
'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
print(l1+l2)'''

#Find the index of the first occurrence of an element from a specific position ?
'''
l=[1,2,3,2,4]
print(l.index(2))'''

#Remove and return the last element from a list ?
'''l=[1,2,3,4,5]
print(l.pop(-1))
print(l)'''

#Find the second largest element in a list
'''
l=[2,3,4,5,6,6,5]
m=l[0]
s=0
for i in l:
    if i>m:
        s=m
        m=i
    elif i>s and i!=m:
        s=i
print(m,s)'''

#Remove elements at even indices from a list
'''
l=[5,6,7,3,2,1,1]
for i in range(len(l)-1,-1,-1):
    if i%2==0:
        del l[i]
print(l)'''

