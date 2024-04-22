from Organisms.organism import OrganismInitialData
from Organisms.plant import Plant


class Guarana(Plant):
    def __init__(self, name, row, column):
        strength = OrganismInitialData[name]["strength"]
        initiative = OrganismInitialData[name]["initiative"]
        character = OrganismInitialData[name]["character"]
        super().__init__(strength, initiative, name,
                         character, row, column, "guarana.png")

    def action(self):
        pass

    def collision(self):
        pass