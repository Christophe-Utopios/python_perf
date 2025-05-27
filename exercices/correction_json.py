import os, json

filename = "music.json"
folderpath = os.path.join(os.curdir, "datas")
list_music = []


def init():
    global list_music

    if not os.path.exists(folderpath):
        os.mkdir(folderpath)
        pass

    if os.path.exists(fullpath):
        with open(fullpath, mode='r') as file:
            list_music = json.load(file)
    else:
        list_music = []


fullpath = os.path.join(folderpath, filename) # /exercices/datas/music.json


def save():
    with open(fullpath, mode='w') as file:
        json.dump(list_music, file, indent=4)


def get_score_from_user():
    score = 0
    while True:
        try:
            score = int(input("Score de la chanson (sur 5) : "))
            if 0 <= score <= 5:
                break
            else:
                raise ValueError
        except ValueError:
            print("Il faut un score compris entre 0 et 5 !")
    return score


def ajouter_chanson():
    print("\n === AJOUTER UNE CHANSON ===")
    new_titre = input("Titre de la chanson : ")
    new_artiste = input("Artiste de la chanson : ")
    new_categorie = input("Catégorie de la chanson : ")
    new_score = get_score_from_user()
    new_chanson = {'Titre': new_titre, 'Artiste': new_artiste, 'Catégorie': new_categorie, 'Score': new_score}

    list_music.append(new_chanson)
    pass


def voir_chansons():
    print("\n === LISTE DES CHANSONS ===")
    for index, item in enumerate(list_music):
        print(f"""{index} : {item['Titre']} par {item['Artiste']}
      Catégorie : {item['Catégorie']}
      Score : {item['Score']}""")
    pass


def editer_chanson():
    print("\n === EDITER UNE CHANSON ===")
    index_cherche = int(input("Quel est l'ID de chanson que vous voulez modifier ? "))

    chanson_trouvee = list_music[index_cherche]
    if chanson_trouvee is not None:
        new_titre = input("Titre de la chanson : ")
        new_artiste = input("Artiste de la chanson : ")
        new_categorie = input("Catégorie de la chanson : ")
        new_score = get_score_from_user()
        chanson_trouvee['Titre'] = new_titre
        chanson_trouvee['Artiste'] = new_artiste
        chanson_trouvee['Catégorie'] = new_categorie
        chanson_trouvee['Score'] = new_score
    else:
        print("Il n'y a pas de chanson possédant cet ID !")
    pass


def supprimer_chanson():
    print("\n === SUPPRIMER UNE CHANSON ===")
    index_cherche = int(input("Quel est l'ID de chanson que vous voulez supprimer ? "))

    chanson_trouvee = list_music[index_cherche]
    if chanson_trouvee is not None:
        list_music.remove(chanson_trouvee)
    else:
        print("Il n'y a pas de chanson possédant cet ID !")
    pass


def menu_principal():
    init()

    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Ajouter une chanson")
        print("2. Voir les chansons")
        print("3. Editer une chanson")
        print("4. Supprimer une chanson")
        print("0. Quitter le programme")

        choix_user = int(input("Faites votre choix : "))
        if choix_user == 0:
            break
        elif choix_user == 1:
            ajouter_chanson()
        elif choix_user == 2:
            voir_chansons()
        elif choix_user == 3:
            editer_chanson()
        elif choix_user == 4:
            supprimer_chanson()
        else:
            print("Ce choix n'est pas valide !")

        print("")

    save()


menu_principal()
