def contains_duplicate(nums):
    repeatedSet=set()
    for element in nums:
        if element in repeatedSet:
            return True
            
        repeatedSet.add(element)
    return False
        
nums = [1,2,3,1]
print(contains_duplicate(nums))
    
