"""
search.py   基本查找方法训练

"""
l=[3,1,2,6,5,8,4,7,9]
l.sort()
#对有序数列进行二分查找
def search(list_,key):
    low,high=0,len(list_)-1
    while low<=high:
        mid=(low+high)//2
        if list_[mid]<key:
            low=mid+1
        elif list_[mid]>key:
            high=mid-1
        else:
            return mid


print("key index is:",search(l,6))