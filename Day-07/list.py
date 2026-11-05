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





            

    
    