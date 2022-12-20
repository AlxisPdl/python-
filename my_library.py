import random

def randint_list(lower_value: int, higher_value: int, count: int=10) -> list:

    numbers =[]

    for i in range(0, count):
      number = random.randint(lower_value, higher_value)
      numbers.append(number)

    return numbers

my_list = randint_list(50, 100, 4)
print(my_list)

def my_average(numbers: list) -> float:

    my_sum = 0

    for number in numbers:
        my_sum =+ number

    result = my_sum / len(numbers)
 
    return result



def my_average2(numbers: list) -> float:

    my_sum = 0

    for number in numbers:
        if type(number) is int or type(number) is float:
            my_sum =+ number

    result = my_sum / len(numbers)
 
    return result

my_liste = [42, True, 'abc', 123]
result = my_average2(my_liste)
print(result)