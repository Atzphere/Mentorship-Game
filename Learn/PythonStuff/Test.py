class Animals:
    speciesGlobal = "dog"
    faveFoodGlobal = "bone"

    def displayStats(self):
        print(self.speciesGlobal, self.faveFoodGlobal)

    def __init__(self, species, faveFood):
        self.speciesGlobal = species
        self.faveFoodGlobal = faveFood



