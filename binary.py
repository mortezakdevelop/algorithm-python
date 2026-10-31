numbers = [12, 5, 28, 9, 34, 17, 25, 45 , 11]
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
        

