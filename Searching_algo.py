def binary_search(list, n, t,step):
    s = 0
    e = n-1
    while s <= e:
        step=step+1
        m = s+(e-s)//2  
        if list[m] == t:
            return m
        elif list[m] > t:
            e = m-1
        else:
            s = m+1
    return -1


# Create a list
#Using binary_Search Algorithm
list = []
n = int(input("Enter the length of the list: "))
step=1
for i in range(n):
    f = int(input())
    list.append(f)
list.sort()
t = int(input("Enter the number that you want to find: "))
ans = binary_search(list, n, t,step)
if ans == -1:
    print("Target is not present in list")   
else:
    print("The number", t, "is present at index using binary search: ", ans)
    

#Using Linear search Algorithm
h=0
step1=0
for i in range(0,n):
    step1=step1+1
    if list[i]==t:
        h=h+1
        print("The number is present at index using linear search: ",i)
        print("Total number of steps in linear search are: ",step1)
        break    
if h==0:
    print("Number not find")



#Using Fibonnacci Search Algorithm
def fun(list,key):
    f2=0
    f1=1
    f=1
    while f<n:
        f2=f1
        f1=f
        f=f1+f2

    i=0
    offset=0
    while f>1:
        i=min(offset+f2,n)
        if t<list[i]:
            f=f2
            f1=f1-f2
            f2=f-f1
        elif t>list[i]:
            f=f1
            f1=f2
            f2=f-f1
            offset=i
        else:
            print(t,"found at using fibonnaci search: ",i)
            return True
    return False
        
list.sort()
print(fun(list,t))