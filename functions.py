from collections.abc import Callable
import random
import my_library 

def addition(a: float, b: float) -> float:
    """cette fonction permet d'additionner deux nombres

    a float le premier nombre à additioner
    b float le deuxième nombre à additioner
    return float le résultat de l'addition
    """
    result = a + b 

    return result

result = addition(123, 42)
print(result)

my_number1 = 123
my_number2 = 42

result = addition(my_number1, my_number2)
print(result)

def calculer(calcul1: Callable, calcul2: Callable, a:float, b: float, c:float) -> float: 
    result = calcul1(a, b)
    result = calcul2(result, c)

    return result

result = calculer(addition, addition, 123, 42, 14)
print(result)


def randint_list(lower_value, higher_value, count):

    numbers =[]

    for i in range(0, count):
      number = random.randint(lower_value, higher_value)
      numbers.append(number)

    return numbers

my_list = randint_list(0, 100, 10)
print(my_list)

my_list = my_library.randint_list( 0, 100, 10)
print(my_list)

# ecrire une fonction qui accepte en pararmetre une liste et qui renvoie la moyenne de nombres de la liste

# reponse exo apprenant

def moyennelist(liste:list) -> float:     
    somme = 0     
    for i in range(len(liste)):         
        somme += liste[i]
        moyenne = somme/len(liste)  
    
    return moyenne 

liste = [5,5,5,5,5] 
print(moyennelist(liste))