# l'opérateur d'affectation  = permet d'injecter une valeur dans une variable
# integer
my_number1 = 123
my_number2 = -42
print(my_number1)
print(my_number2)

# float
my_number3 = 3.14
my_number4 = -2.71
my_number5 = 0.0
print(my_number3)
print(my_number4)
print(my_number5)

#booleen
my_boolean1 = True
my_boolean2 = False
print(my_boolean1)
print(my_boolean2)

#none valeur nulle
my_none = None
print(my_none)
print(type(None))

# type pour connaitre le type
print(type(my_number1))
print(type(my_number3))
print(type(my_boolean1))

#string chaine de caractère
my_text1 = "ceci est une chaine de caractère"
my_text2 = 'ceci est aussi une chaine de caractère'
print(my_text1)
print(my_text2)

# \ caractère d'échappement
# \n saut de ligne
my_text3 = "ef\varv\nazga"

# """ entrée est un saut de ligne 
print(my_text3)
my_text4 = """abc
ezf
fef"""
print(my_text4)

#permutation de la valeur des variables
a = 123
b = 42
a,b = b, a
print(a, b)

a = 123
b = 42
c = a
a = b
b = c
print(a,b)

# varirante qui ne marche qu'avec des nombres
# c = a + b
# a = a - c
# b = c - b

# transtypage
foo = "123"
foo = int(foo)
print(type(foo))
foo = float(foo)
print(type(foo))
# float vers str
foo = 3.14
foo = str(foo)
print(foo)

#
foo = 2.71
a = int(foo)
b = foo - a
print(a, b)

# trastypage == type casting == conversion d'un type de données

# 0 donne False et tous les autres nombres donnent True
my_number7 = 10
print(bool(my_number7))

# conversion impicitite en bouléen
if (my_number7):
    print("L'utilisateur a mis autre chose que zéro")

else:
    print("l'utilisateur a mis zéro")


# listes
fruits = ['ananas', 'banana', 'cerise']

# operateur d'inclusion*
result = 'ananas' in fruits
print(result)
result = 'fraise' in fruits
print(result)
if fruits:
    print("La liste contient des elements")
else:
    print("La liste ne contient aucun element")
    