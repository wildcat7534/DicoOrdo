class DicoOrdo(object):
    """Lesson from OpenClassrooms :
    https://openclassrooms.com/courses/235344-apprenez-a-programmer-en-python/233322-tp-un-dictionnaire-ordonne"""

    def __init__(self, **dico): # Creation of an empty Dict, OR with ** : adding some data into a Dict
        self.dico = dico
        self.d = self.dico      # Need to use a second Dict for the Def __add__

    def items(self):
        return self.dico.items()

    def keys(self):
        return self.dico.keys()

    def values(self):
        return self.dico.values()

    def __repr__(self):

        return ("{}".format(self.dico))

    def __setitem__(self, key, value):      # When we want use the Dict's habits : dict[key]: value
        (self.dico).update({key: value})

    def __getitem__(self, item):            # To get value from a key : dict['key']
        return self.dico[item]

    def __add__(self, other):               # For adding 2 Dict together
        self.d.update(other.dico)
        return self.d

    def sortByKey(self):                    # Ordonnary the Dict
        dico_sorted = {}
        for key in sorted(self.dico):
            dico_sorted.update({key: self.dico[key]})
            # print("{}: {}".format(key, self.dico[key]))  # To print a more concentionnal listing
        self.dico = dico_sorted

    def sortByKeyReversed(self):            # Ordonnary inversed the Dict
        dico_reversed = {}
        for key in sorted(self.dico, reverse = True):
            dico_reversed.update({key: self.dico[key]})
            # print("{}: {}".format(key, self.dico[key]))
        self.dico = dico_reversed

    def sort(self):
        """  ERROR : the exercise doesn't ask to sort by Values(!). This 'def' works, but if there is no same
        values...  """
        temp_list = []
        newdico = {}
        for value in sorted((self.dico).values()):
            # newdico = ({self.dico.keys()[value]: value})
            temp_list += (list(self.dico.keys())[list(self.dico.values()).index(value)], value)

        newdico = {temp_list[i]: temp_list[i + 1] for i in range(0, len(temp_list), 2)}
        self.dico = newdico

    def __delitem__(self, key):
        del self.dico[key]

    def __len__(self):
        return len(self.dico)

    def append(self, other):                # I didn't use it ^^!
        assert isinstance(other, DicoOrdo)



fruit = DicoOrdo()
legume = DicoOrdo(carotte = 26, haricot = 48)
magasin = DicoOrdo()
fruit['pomme'] = 52
fruit['poire'] = 34
fruit['prune'] = 128
fruit['melon'] = 15
fruit['banane'] = 153
legume['poivron'] = 29
legume['salade'] = 11

print("\n", fruit, " <--Dict vide\n".upper())

print(fruit," <--Fruits normal.\n".upper())

fruit.sortByKey()
print(fruit, " <--fruits ordonnés par key.\n".upper())

magasin.dico = fruit + legume
print(magasin, " <--tout le magasin.\n".upper())

magasin.sortByKeyReversed()
print(magasin, " <--tout le magasin inversé par KEY.\n".upper())

magasin.sortByKey()
print(magasin, " <--tout le magasin ordonnés par KEY.\n".upper())

del magasin['banane'], fruit['banane']

print(magasin, " <---magasin toujours ordonné et sans 'banane'\n".upper())

print("---->   Il y a {} legume(s) et {} fruit(s). Total : {}"
      " dans le magasin.\n".format(len(legume), len(fruit), len(magasin)))

print(legume['haricot'], " <--- Nbr de 'haricot'?\n")
# for cle in magasin:           # I didn't made it, just this one :(((
#     print(cle)
print(legume.keys())
print(legume.values(),"\n")

for k, v in legume.items():
    print ("{} ({}) <--- listing des ITEMS de 'legume'.".format(k, v))