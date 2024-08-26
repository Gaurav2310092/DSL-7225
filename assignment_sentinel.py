#Searching using Sentinel Search
#creating a list 
list=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    m=int(input())
    list.append(m)
key=int(input("Enter the number that have to find: "))
list.append(key)
i=0
step=0
while(list[i]!=key):
    step=step+1
    if(list[i]==key):
        break
    else:
        i=i+1
if(i<n):
    print(key,"found at index ",i)
    print("Total number of step in sentinel search are: ",step)

else:
    print(key," not found")