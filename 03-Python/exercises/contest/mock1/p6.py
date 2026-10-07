# P6 —— 题面见同目录 README.md

# TODO:
n,q=map(int,input().split())
nums=list(map(int,input().split()))
for _ in range(q):
    k=int(input())
    left=0
    right=n-1
    first=-1
    last=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<k:
            left=mid+1
        elif nums[mid]==k:
            first=mid
            right=mid-1
        elif nums[mid]>k:
            right=mid-1

    left=0
    right=n-1
    while left<=right:
            mid=(left+right)//2
            if nums[mid]<k:
                left=mid+1
            elif nums[mid]==k:
                last=mid
                left=mid+1
            elif nums[mid]>k:
                right=mid-1
    print(first,last)
