import random
def create_nums():
    nums=[]
    for i in range(20):
        a=random.randint(0,100)
        nums.append(a)
    return nums
def sort(nums,flag,begin,end):
    #flag=range(len(nums))#flag is used to remenber the positon of objects in nums
    empty=begin
    a=nums[begin]
    b=flag[begin]
    i=begin+1
    j=end
    for k in range(end-begin):
        if i>empty:
            if nums[i]<=a:
                nums[empty]=nums[i]
                flag[empty]=flag[i]
                empty=i
                i=i+1
            elif nums[j]>a:
                j=j-1
            else:
                nums[empty]=nums[j]
                flag[empty]=flag[j]
                empty=j
                j=j-1
        elif j<empty:
            if nums[j]>a:
                nums[empty]=nums[j]
                flag[empty]=flag[j]
                empty=j
                j=j-1
            elif nums[i]>a:
                nums[empty]=nums[i]
                flag[empty]=flag[i]
                empty=i
                i=i+1
            else:
                i=i+1
    nums[empty]=a
    flag[empty]=b
    #print nums
    #print flag
    if begin<empty-1:
        sort(nums,flag,begin,empty-1)
    if end>empty+1:
        sort(nums,flag,empty+1,end)
    return nums
    
def sort2(nums,begin,end):
    empty=begin
    a=nums[begin]
    i=begin+1
    j=end
    for k in range(end-begin):
        if i>empty:
            if nums[i]<=a:
                nums[empty]=nums[i]
                empty=i
                i=i+1
            elif nums[j]>a:
                j=j-1
            else:
                nums[empty]=nums[j]
                empty=j
                j=j-1
        elif j<empty:
            if nums[j]>a:
                nums[empty]=nums[j]
                empty=j
                j=j-1
            elif nums[i]>a:
                nums[empty]=nums[i]
                empty=i
                i=i+1
            else:
                i=i+1
    nums[empty]=a
    #print nums
    if begin<empty-1:
        sort(nums,begin,empty-1)
    if end>empty+1:
        sort(nums,empty+1,end)
    #return nums
def main():
    nums=create_nums()
    print nums
    flag=range(len(nums))
    a=sort(nums,flag,0,19)
    print flag
    print nums
    n=range(20)
    for i in range(20):
        n[flag[i]]=nums[i]
    print n
main()
    
    
        
            
                
                
                
                
            
        
        
        
    
    
        
        
