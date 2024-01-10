# object-oriented programming

type(3),type(3.),type('azerty'),type([1,2,3]),type((3,4,'GGFD')),type({'boire':'avaler un liquide'})
# repsonse: (int, float, str, list, tuple, dict)
type(type),type(None),type(True)
# response: (type, NoneType, bool)

class Car:
    def __init__(self):
        self.name = "Ferrari"





class Person:
    def __init__(self, name, firstname, birthday):
        self.name = name
        self.firstname = firstname
        self.age = 30
        self.place_residence = "Bruxelles"
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}, {self.firstname}, {self.age}, {self.place_residence}, {self.birthday}"

mySelf = Person('Careme', 'Lidwine', '01/04/1993')
print(mySelf)




class Counter:
    # C'est un attribut de classe, partagé par toutes les instances de Counter
    objects_created = 0  
    def __init__(self):
        # Chaque fois qu'un objet est créé, on incrémente cet attribut
        Counter.objects_created += 1


# Au début, aucun objet Counter n'a été créé, donc objects_created est égal à 0
print(Counter.objects_created)

# Créons un premier objet Counter
a = Counter()
# Maintenant, un objet a été créé, donc objects_created est égal à 1
print(Counter.objects_created)

# Créons un deuxième objet Counter
b = Counter()
# Maintenant, deux objets ont été créés, donc objects_created est égal à 2
print(Counter.objects_created)
# Chaque fois qu'un nouvel objet Counter est créé, l'attribut est incrémenté




# classe Blackboard est créée avec un attribut de classe appelé surface qui représente la surface de la table. Lorsqu'un objet de la classe Blackboard est créé, l'attribut surface est initialisé à une chaîne vide.
class Blackboard:
    def __init__(self):
        self.surface = ""
    # méthode write est définie pour écrire sur la surface de la table. Si la surface n'est pas vide, un saut de ligne est ajouté avant d'ajouter le message écrit.
    def write(self, message_written):
        if self.surface != "":
            self.surface += '\n'
        self.surface += message_written

    # Définition des méthodes read et reset :
    # Les méthodes read et reset sont définies mais non implémentées. 
    def read(self):
    # Cette méthode est chargée d'afficher, grâce à print,
    # la surface de la peinture
        print(self.surface)

    def reset(self):
        # Cette méthode permet d'effacer la surface de la table
        self.surface = ""


# Création d'une instance de la classe Blackboard
tab = Blackboard()
# Check if blackboard is empty
# print(tab.surface)
# Lecture de la surface (qui est initialement vide)
tab.read()
# Écriture de messages sur la surface
tab.write("Coooool ! Il love this one")
# print(tab.surface)
tab.write("Have a good start to the school year!")
# print(tab.surface)
tab.write('Hello Swartz')
Blackboard.write(tab,'Hello Turing')
print(tab.surface)

help(Blackboard)

Blackboard.write(tab, "try")
print(tab.surface)
# Lecture de la surface après avoir écrit des messages
tab.read()
# Réinitialisation de la surface
tab.reset()
# Lecture de la surface après réinitialisation (devrait être vide)
tab.read()
# Affichage de l'aide pour la classe Blackboard
help(Blackboard)

dir(Blackboard)

Blackboard.__dict__

