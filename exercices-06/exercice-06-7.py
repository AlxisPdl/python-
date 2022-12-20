# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

mon_mot = my_list[1]

print(my_list)

my_list[1] = my_list[3]

print(my_list)

my_list[3] = mon_mot 

print(my_list)