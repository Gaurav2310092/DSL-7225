#Sorting a list using bubble sort
l = [90,3,45,62,13,24,1,10]
def bubblesort(l):
    n=len(l)
    print("Unsorted list :",l)
    for i in range(1,n):
        h=0
        for j in range(0,n-i):
            if(l[j] > l[j+1]):
                h=h+1
                l[j],l[j+1] = l[j+1],l[j]
        if h==0:
            break
    return l

#Sorting a list using Selection sort
a = [11,25,1,90,78]
def selection_sort(a):
    f=len(a)
    print("Unsorted list :",a)
    for i in range(0,f-1):
        p = i
        for j in range(i,f):
            if(a[p]>a[j]):
                 p = j

        a[i],a[p] = a[p],a[i]
        

    return a        

#Sorting a list using Insertion sort
b = [67,34,23,12,4,9,99,78,37]
def insertion_sort(b):
    g=len(b)
    print("Unsorted list :",b)
    i=1
    while i<g:
        x=b[i]
        j=i-1
        while j>=0 and b[j]>x:
            b[j+1]=b[j]
            j=j-1
        b[j+1]=x
        i=i+1
    return b

#Sorting a list using Shell sort
d = [99, 10, 78, 86, 33, 42, 23, 12,67]
def shell_sort(d):
    print("unsorted list:",d)
    s = len(d)
    gap = s // 2
    while gap >=1:
        for i in range(gap, s):
            x = d[i]
            j = i
            while j>=gap and d[j-gap]>x:
                d[j]=d[j-gap]
                j-=gap
            d[j]=x
        gap=gap//2
    return d

print("Using Bubble sort -- ")
print("Sorted list : ",bubblesort(l))
print(" \nUsing selection sort -- ")
print("Sorted list : ",selection_sort(a))
print(" \nUsing insertion sort -- ")
print("Sorted list : ",insertion_sort(b))
print(" \nUsing shell sort -- ")
print("Sorted list : ",shell_sort(d))
