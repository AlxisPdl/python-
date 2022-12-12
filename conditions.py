import random

if True: 
    print("Le savoir est une arme.")
    print("Mais une arme n'est pas le savoir")

if False: 
    print("Le savoir est le savoir")
    print("Mais le savoir n'est pas le savoir")


conditions_vente = True

if conditions_vente: 
    print("L'utilisateur a accepter les conditions de vente.")

else: 
    print("L'utilisateur n'as pas accepter les conditions de vente.")

if not False : 
    print("L'utilisateur n'as pas accepter les conditions de vente.")

else : 
    print("L'utilisateur a accepter les conditions de vente.")


emails = random.randint(0, 3)

# elif est la même chose que else if 

if emails == 1:
    print("Vous avez un nouveau mail")
elif emails > 1:
    print(f"Vous avez {emails} nouveaux mails")
else:
    print("Vous n'avez pas de nouveaux mails")

windows_closed = bool(random.randint (0, 1))
electricity_off = bool(random.randint (0, 1))
print(f'{windows_closed = }')
print(f'{electricity_off = }')

if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("l'électicité est coupée")

elif not windows_closed and electricity_off:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité est coupée")

else:
    print("Les fenêtres sont fermées")
    print("L'électricité n'est pas coupée")

bank_card = True
cash = True

print(f'{bank_card = }')
print(f'{cash = }')


if bank_card or cash: 
    print ("On a un moyen de paiement")

    if bank_card:
        print ("On a la carte bancaire")

    if cash:
        print ("On a du liquide")

else:
    print("On a aucuns moyens de paiement")



ticket = True
vip = False
registration = False

print(f'{ ticket = }')
print(f'{ vip = }')
print(f'{ registration = }')


#Quand on mélange or et and on utilise systematiquement des prarenthèses.


if (ticket or vip) and registration:
    print ("Access Authorized")

else:
    print ("Access Denied")

product_count = random.randint(0, 50)

if product_count > 20:
    print ("il y'a plus de 20 articles")
    print ("ras")

elif 5 < product_count <= 20:
    print("Il y'a plus que 5 articles")
    print("Alerte approvisionnement")

elif 0 < product_count <= 5 :
    print("Il y'a plus que 5 articles")
    print("Alerte rupture imminente")

else:
    print("Il n'y a plus de produits")
    print("Alerte rupture")

product_count = 6

if product_count > 5:
    print ("Il y'a plus que 5 articles ")

    if product_count <= 20:
        print("Il y'a 20 ou moin d'articles")

