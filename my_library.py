import random

def randint_list(lower_value, higher_value, count):

    numbers =[]

    for i in range(0, count):
      number = random.randint(lower_value, higher_value)
      numbers.append(number)

    return numbers

my_list = randint_list(50, 100, 4)
print(my_list)