a = [4,5,6,9]
# num = max(a)
new=[]
k = 4
for i in range(0,len(a)):
    new.append(max(a[i:i+k]))
    
    if(a[i]):
        new.append(i)

for i in range(0,len(new)):

    if a[i-1] < a[i]:
        new = a[i:i+k]
        break
    elif a[i-1] > a[i]:
        new = a[i-1:i+k-1]
        break
print new
