from Organisms.organism import OrganismInitialData
from Organisms.animal import Animal


class Fox(Animal):
    def __init__(self, name, row, column):
        strength = OrganismInitialData[name]["strength"]
        initiative = OrganismInitialData[name]["initiative"]
        character = OrganismInitialData[name]["character"]
        super().__init__(strength, initiative, name, character, row, column, "fox.png")

    def action(self):
        pass

    def collision(self):
        pass
