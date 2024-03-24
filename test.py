def recursive_nums(num):
    if num<=0: #non-positive nums
        return 0
    elif num % 2 ==0: #even nums
        return num + recursive_nums(num-1)
    else: #odd nums
        return recursive_nums(num-1) 
    
print (recursive_nums(6))