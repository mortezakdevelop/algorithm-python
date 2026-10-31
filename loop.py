numbers = [3, 7, 10, 12, 15, 20, 21, 30]

result = [
    number * 10 if number % 2 == 0 else number * 100
    for number in numbers
]

result = [
    number ** 2 if number % 3 == 0 and number > 10 else number
    for number in numbers
    
]


print(result)