fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x:x % 2 != 0, fibonacci))
print(odd_numbers)
[1,1,3,5,13,21,55]
even_numbers = list(filter(lambda x:x % 2 == 0, fibonacci))
print(even_numbers)
[0,2,8,34]
# or alternatively:
even_numbers = list(filter(lambda x:x % 2 - 1, fibonacci))
print(even_numbers)