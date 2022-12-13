my_text1 = """ Voici un text 
multi-ligne
abc
foo
bar"""

print(my_text1)

#On utilise "\n" pour un saut de ligne.

my_text2 = " Voici un text\nmulti-ligne\nabc\nfoo\nbar"

print(my_text2)

number1 = 123
my_text3 = f"Nombre = {number1}"

print(my_text3)

my_text4 = f"""
Le nombre 
est
{number1}
foo
"""

print(my_text4)

my_text5 = f"""
{{
foo
}}
{{bar}}
"""
print(my_text5)

# concaténation d'une chaîne de caractères.

my_number2 = 3.14
my_text6 = "Le nombre PI est " + str(my_number2)

print(my_text6)

# Tronquer un float dans une interpolation.
# .4f signifie 4 chiffres après la virgule.

my_number3 = 1 / 3 
my_text7 = f"1 / 3 ~= {my_number3:.4f}"

print(my_text7)

#Les interpolations acceptent les expressions.

my_text8 = f"1 + 1 = {1 + 1}"
print(my_text8)

# l'écriture d'une documentation pour une fonction.

def hello(name: str) -> None:

    """Cette fonction dit bonjour a quelqu'un 

    name str indique le nom de la personne à saluer return None
    """

    print(f"Salut {name}")

# appel d'une fonction

hello('Toto')
#print(help)

my_text9 = "Lorem ipisum blabla bla j'parle latin tahu"
#longueur d'une str
my_number4 = len(my_text9)
print(my_number4)

#trouve la position d'une str dans une autre str
my_number5 = my_text9.find('Lorem')
print(my_number5)

my_number6 = my_text9.count ('ipsum')
print(my_number6)

#Remplacement de text non permanent 
print(my_text9.replace('Lorem', 'foo'))
print(my_text9)

#remplacement de text permanent
my_text9=my_text9.replace('Lorem', 'foo')
print(my_text9)

#eclate une str en liste en utilisant l'espace en caractère de séparations des éléments

my_list1 = my_text9.split()
print(my_list1)

#la fonction "len" peut être aussi tulisée avec des listes pour compter le nombre d'élements 

print(len(my_list1))

#accès en lecture au 0ème au 10ème caractère de la str
print(my_text9[0:10])

#accès en lecture du 10ème a la fin de la str
#les zéro ne sont pas obligatoires
print(my_text9[10:])

#la chaine de caractère sera lu de la fin jusqu'au debut grave au :-1 ajouter entre les crochets.
print(my_text9[::-1])


#permet la lecture d'un caractères sur deux 
print(my_text9[::2])

