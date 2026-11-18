numbers = [4, 9, 15, 21, 28, 36, 44, 53, 67]
numbers_two = [1, 3, 5, 7, 7, 7, 9, 11, 13]
numbers.sort()
target = 28
left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2
    
    if numbers[mid] ==  target:
        print("index of target", mid)
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid -1
        
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right :
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1


def binary_search_find_first_index_of_target(numbers):
    left = 0
    right = len(numbers) - 1
    target = 15
    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == target:
            if  mid > 0 and numbers[mid -1] == target:
                right = mid - 1
            else:
                return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def last_or_first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            #left = mid + 1
            right = mid - 1

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result

def first_occurrence(numbers,target):
    left = 0
    right = len(numbers) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            result = mid
            right = mid - 1
        elif numbers[mid] < target:
            left = mid  + 1
        else:
            right = mid - 1
    return result

def last_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            result = mid
            left = mid + 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def count_occurrence(numbers,target):
   count = 0
   count = last_occurrence(numbers,target) - first_occurrence(numbers,target) + 1
   if first_occurrence(numbers,target) == -1:
       return 0
   return count

#search insert binary code
def find_nearest_index_of_number(numbers,target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return left
            

print(find_nearest_index_of_number(numbers,1))
          
    
            
            
            
     




        

