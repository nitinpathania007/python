def mergesort(nums):
    
    n=len(nums)

    if n==1:
        return nums
    if n==2:
        if nums[0] < nums[1]:
            return nums
        else:
            nums[0],nums[1] = nums[1],nums[0]
            return nums
    else:

        sortedfirst = mergesort(nums[0:(n//2)])
        sortedsecond = mergesort(nums[(n//2):])

        finalsorted=[]

        firstindex=0
        secondindex=0

        firstlen=n//2
        
        secondlen=(n//2) + (n % 2)
        
        while (firstindex < firstlen) and (secondindex < secondlen):
            if sortedfirst[firstindex] < sortedsecond[secondindex]:
                finalsorted.append(sortedfirst[firstindex])
                firstindex += 1
            else:
                finalsorted.append(sortedsecond[secondindex])
                secondindex += 1


        if firstindex < firstlen:
            finalsorted.extend(sortedfirst[firstindex:])
        else:
            finalsorted.extend(sortedfirst[secondindex:])
        
        return finalsorted

def selectionsort(nums):

    finalsorted=[]
    n=len(nums)
    minspot = 0
    
    for i in range(0,n-1):
        newminindex = minspot

        for index in range(minspot+1,n):
            if nums[index] < nums[newminindex]:
                newminindex = index
                
        nums[minspot],nums[newminindex] = nums[newminindex],nums[minspot]
        minspot += 1
    return nums


file=open("data10.txt","r")

numstrings=file.readlines()

file.close()

for i in range(0,len(numstrings)):
    numstrings[i] = int(numstrings[i])

#numbers=[10,62,83,17,23,88,44,33,101,1]

#sortnums=mergesort(numstrings)

#print(sortnums)


sortnums1=selectionsort(numstrings)

print(sortnums1)
