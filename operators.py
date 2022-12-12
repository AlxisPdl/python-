import random
import math

# = affectation
foo = 123

# + addition
foo = 123+ 42
foo = foo + 42 # ou foo += 42 (operateur d'incrementation)

# - soustraction
foo = foo - 42
foo = foo - 42 # ou foo -= 42 (operateur de decrementation)

# / division
foo = 123 / 42
print(foo)

# // division entière
foo = 123 // 42
print(foo)

# % modulo
foo = 4 % 3
foo = random.randint(1,100)
print(foo % 2)

# * multplication


# ** puissance
foo = 2**2
foo = 2**3
foo = 2**4
print(foo)

# ^ puissance mais pas en python
# sqrt() racine carée 
foo = math.sqrt(4)
foo = 4 ** (1/2)
print(foo)

# les opérateurs de comparaison, ne pas confondre avec l'affectation
# ou l'identité === qui n'existe pas en python
result = 1 == 1
print(result)

#les grandeurs
result = 123 < 42
print(result)

result = 123 <= 42
print(result)

result = 123 != 42
print(result)

# les intervalles
# < > ou <= =>
my_number = random.randint(0,100)
result = 0 <= my_number < 50
print (result)

# operateur and (et)

result = True and False
print(result)
result = False and True
print(result)
result = True and True 
print(result)
result = False and False
print(result)

a = random.randint (0, 1)
b = random.randint (0, 1)
result = bool(a) and bool(b) 
print(a, b)
print(result)

# operateur or (ou)

result = True and False
print(result)
result = False and True
print(result)
result = True and True 
print(result)
result = False and False
print(result)

a = random.randint (0, 1)
b = random.randint (0, 1)
result = bool(a) and bool(b) 
print(a, b)
print(result)


# operateur not

result = not True
print(result)
result = not False 
print(result)