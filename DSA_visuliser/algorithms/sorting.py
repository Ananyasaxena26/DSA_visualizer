def bubble_sort(arr):
    steps=[]
    a = arr.copy()
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            steps.append((a.copy(),j,j+1))
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                steps.append((a.copy(),j,j+1))
    return steps

def merge_sort(arr):
    steps=[]
    def merge(a,l,m,r):
        left = a[l:m+1]
        right = a[m+1:r+1]
        i=j=0
        k=l
        while i<len(left) and j<len(right):
            steps.append((a.copy(),k,None))
            if left[i]<right[j]:
                a[k]=left[i]; i+=1
            else:
                a[k]=right[j]; j+=1
            k+=1
        while i<len(left):
            steps.append((a.copy(),k,None))
            a[k]=left[i]; i+=1; k+=1
        while j<len(right):
            steps.append((a.copy(),k,None))
            a[k]=right[j]; j+=1; k+=1

    def ms(a,l,r):
        if l>=r: return
        m=(l+r)//2
        ms(a,l,m)
        ms(a,m+1,r)
        merge(a,l,m,r)

    b = arr.copy()
    ms(b,0,len(b)-1)
    for step in steps:
        steps.append(step)
    return steps
