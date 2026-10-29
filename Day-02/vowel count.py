s=input().split()
v='AEIOUaeiou'
for word in s:
    c=0
    for char in word:
        if char in v:
            c+=1
    print(f' {word} : {c}')
            
