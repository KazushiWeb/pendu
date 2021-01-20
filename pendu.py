from getpass import getpass

mot  = getpass("Entre votre mot")

list=[]
votre_liste=[]


for x in mot:
    liste.apprend(x)
    votre_liste.apprend('*') 

print("".join(votre_liste))

nb_erreur = 0
while nb_erreur < 9 :
    lettre = imput("Entrez votre lettre")

    if len(lettre)>1:
        if lettre ==mot:
            print("vous avez trouvé")
            break

    if lettre in liste:
        for (index,y) in enumerate(liste):
            if y==lettre:
                votre_liste[index] = x
        v = "".join(votre_liste)
        print("bonne lettre",v)

        if list==votre_liste:
            print("vous avvez trouvé")
    else:
        nb_erreur +=1
        print('Mauvais lettre, il vous reste %s essais'%9-nb_erreur())

        if nb_erreur ==9:
            print(' vous avez perdu')