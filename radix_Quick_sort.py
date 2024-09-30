#Using counting sort
def counting_sort(a, exp):
    n = len(a)
    output = [0] * n  
    count = [0] * 10  

    for i in range(n):
        index = (a[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (a[i] // exp) % 10
        output[count[index] - 1] = a[i]
        count[index] -= 1
        i-= 1

    for i in range(n):
        a[i] = output[i]
 

def radix_sort_counting(a):
    max_num = max(a)
    exp = 1  
    step=0
    while max_num // exp > 0:
        step+=1
        counting_sort(a, exp)
        exp *= 10
    print("The no of comaprision in radix sort using counting sort is: ",step)
#------------------------------------------------------------------#


#Using Bucket sort
def radix_sort_bucket(arr):
    ma = max(arr)
    exp = 1
    while ma // exp > 0:
        bucket = [[] for _ in range(10)]
        
        for num in arr:
            digit = (num // exp) % 10
            bucket[digit].append(num)
        
        index = 0
        count=0
        for b in bucket:
            for num in b:
                arr[index] = num
                index += 1
        exp *= 10



#-------------------------------------------------------------------
#Using Quick sort
def partition(b, l, h):
    pivot = b[l]
    i = l
    j = h
    while i < j:
        while i <= h and arr[i] <= pivot:
            i += 1
        while b[j] > pivot:
            j -= 1
        if i < j:
            b[i], b[j] = b[j], b[i]
    b[l], b[j] = b[j], b[l]
    return j

def quick_sort(b, s, e):
    if s < e:
        p = partition(b, s, e)
        quick_sort(b, s, p - 1)
        quick_sort(b, p + 1, e)


# Example usage
n = int(input("Enter the number of elements in the list: "))
a=[]
arr = []
b=[]
for i in range(n):
    m = int(input())
    arr.append(m)
    a.append(m)
    b.append(m)

print("Original array:", a)
radix_sort_counting(a)
print("Sorted array using radix sort and counting sort : ", a)
radix_sort_bucket(arr)
print("Sorted array using radix sort and bucket sort : ",arr)


print("\nOriginal array :",b)
quick_sort(b, 0, len(b) - 1)
print("Sorted array using quick sort is : ", b)
