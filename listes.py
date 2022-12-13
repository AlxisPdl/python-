fruits = ['ananas', 'banane', 'cerise']
print(fruits)

# accès en lecture du 0ème element de la liste
print(fruits[0])

my_fruit = fruits[0]
print(my_fruit)

# accès en ecriture du 0ème element de la liste
fruits[0] = 'abricot'
print(fruits)
print(fruits[0])

my_count = len(fruits)
print(my_count)

index = 0 
if index < my_count:
    print(fruits[index])
    print(f'{index =}')

index += 1
if index < my_count:
    print(fruits[index])
    print(f'{index =}')

index += 1
if index < my_count:
    print(fruits[index])
    print(f'{index =}')