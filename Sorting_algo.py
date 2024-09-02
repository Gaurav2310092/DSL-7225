#Sorting a list using bubble sort
#Also counting the number of comparision
l =[23, 87, 45, 12, 34, 78, 56, 89, 22, 67]

def bubblesort(l):
    step=0
    n=len(l)
    print("Unsorted list :",l)
    for i in range(1,n):
        h=0
        for j in range(0,n-i):
            step+=1
            if(l[j] > l[j+1]): 
                h=h+1
                l[j],l[j+1] = l[j+1],l[j]
        if h==0:
            break
    print("Number of comparision are: ",step)
    return l

#Sorting a list using Selection sort
#Also counting the number of comparision
a = [23, 87, 45, 12, 34, 78, 56, 89, 22, 67]

def selection_sort(a):
    step=0
    f=len(a)
    print("Unsorted list :",a)
    for i in range(0,f-1):
        p = i
        for j in range(i,f):
            step=step+1
            if(a[p]>a[j]):
                p = j
                a[i],a[p] = a[p],a[i]
    print("Number of comparision are: ",step)
    return a        

#Sorting a list using Insertion sort
#Also counting the number of comparision
b = [23, 87, 45, 12, 34, 78, 56, 89, 22, 67]

def insertion_sort(b):
    step=0
    g=len(b)
    print("Unsorted list :",b)
    i=1
    while i<g:
        x=b[i]
        j=i-1
        while j>=0 and b[j]>x:
            step=step+1
            b[j+1]=b[j]
            j=j-1
        b[j+1]=x
        i=i+1
    print("Number of comparision are: ",step)
    return b

#Sorting a list using Shell sort
#Also counting the number of comparision
d =[23, 87, 45, 12, 34, 78, 56, 89, 22, 67]

def shell_sort(d):
    step=0
    print("unsorted list:",d)
    s = len(d)
    gap = s // 2
    while gap >=1:
        for i in range(gap, s):
            x = d[i]
            j = i
            while j>=gap and d[j-gap]>x:
                step=step+1
                d[j]=d[j-gap]
                j-=gap
            d[j]=x
        gap=gap//2
    print("Number of comparision are: ",step)
    return d

step=0
print("Using Bubble sort -- ")
print("Sorted list : ",bubblesort(l))
print("Number of comaprision in this sorting is ;",step)
print(" \nUsing selection sort -- ")
print("Sorted list : ",selection_sort(a))
print("Number of comaprision in this sorting is ;",step)
print(" \nUsing insertion sort -- ")
print("Sorted list : ",insertion_sort(b))
print("Number of comaprision in this sorting is ;",step)
print(" \nUsing shell sort -- ")
print("Sorted list : ",shell_sort(d))
print("Number of comaprision in this sorting is ;",step)
