#create a list
list=[]
n=int(input("Enter the number of students in a class :"))
sum=0
for i in range(0,n):
    m=int(input())
    sum=sum+m
    list.append(m)
#finding the average marks of the class
avg=sum/n
#Finding highest marks in the class
highest=list[0]
for i in range(1,n):
    if list[i]>highest:
        highest=list[i]

#finding lowest marks in the class\
lowest=list[0]
for i in range(1,n):
    if list[i]<lowest and list[i]!=0:
        lowest=list[i]

#finding absent students int the class
absent=0
for i in range(1,n):
    if list[i]==0:
        absent=absent+1

#finding the frequency of the class
f={}
for i in list:
    if i !=0:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
hf=max(f,key=f.get)     

#finding the number of students passed and failed
ps=0
fs=0
for i in range(0,n):
    if list[i]>=40 and i!=0:
        ps=ps+1
    elif list[i]<40 and i!=0:
        fs=fs+1

pp=(ps/n)*100
fp=(fs/n)*100

print("The average of the class is :",avg)
print("The higest marks in the class is :",highest)
print("The lowest marks in the class is :",lowest)
print("The frequecy of the class  marsk is :",hf)
print("The pecentage of passed students in the class is :",pp)
print("The percentage of failed students in the class is :",fp)