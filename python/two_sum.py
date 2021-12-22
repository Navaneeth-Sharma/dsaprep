import time

def two_sum(numbers, target, type_of_solution=1):
    '''
    Assuming only 1 solution exists, find the indices of the two numbers
    that sum to the target.
    '''
    if type_of_solution == 0:
        t1 = time.clock()
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    t2 = time.clock()
                    print(t2-t1)
                    return [i, j]
        
    
    elif type_of_solution == 1:
        t1 = time.clock()
        d = dict()
        for i,n in enumerate(numbers):
            if target-n in d:
                t2 = time.clock()
                print(t2-t1)
                return [d[target-n], i]
            d[n] = i
    
    elif type_of_solution == 2:
        t1 = time.clock()
        d = dict()
        for i,n in enumerate(numbers):
            try:
                d[target-n]
                t2 = time.clock()
                print(t2-t1)
                return [d[target-n], i]
            except:
                d[n] = i
    
print(two_sum([2,7,11,15], 9, type_of_solution=2))