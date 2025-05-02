# Learn about map and filter functions, and be prepared to explain them in class. Provide examples using these functions with lambda expressions.
# Lambda is small and anonymous function often used for short and simple operations with map() and filter()
# The map() and filter() functions are built-in functions in Python that operate on iterables (lists, tuples) by applying a function to each item.
# map() iterates through each item of iterable and applies function for each of them and returns new iterable result
# filter() returns True and False. It returns new iterable when the function is true for the item inside of the given iterable  
my_list = [1, 2, 3, 4, 5, 6, 7]
squared_numbers = list(map(lambda x: x**2, my_list))
print(squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers)

# 1. is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**1/2) + 1):
        if n % i == 0:
            return False
    return True

is_prime(47)

# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
k = int(input('Enter number: '))
def digit_sum(k):
    sum = 0
    k = list(map(lambda x: int(x), list(str(k))))
    for i in k:
        sum += i
    return sum

digit_sum(k)

# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def pow_n(n):
    new_list = []
    for i in range(1, n):
        if 2**i < n:
            new_list.append(2**i)

    return new_list

pow_n(40)
