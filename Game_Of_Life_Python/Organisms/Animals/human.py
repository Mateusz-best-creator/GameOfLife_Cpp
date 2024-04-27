from Organisms.organism import OrganismInitialData
from Organisms.animal import Animal
import pygame


class Human(Animal):
    def __init__(self, name, row, column, given_strength=-1, given_initiative=-1):
        strength = OrganismInitialData[name]["strength"]
        initiative = OrganismInitialData[name]["initiative"]
        character = OrganismInitialData[name]["character"]
        if given_strength != -1:
            strength = given_strength
        if given_initiative != -1:
            initiative = given_initiative
        super().__init__(strength, initiative, name, character, row, column, "human.png")

    def action(self, grid_board):

        self.previous_row = self.row
        self.previous_column = self.column

        grid_board[self.row][self.column] = 'e'
        self.print_to_journal(
            f"{self.name} from ({self.row}, {self.column}) to ")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.column > 0:
                            self.organism_go_left()
                        running = False
                    elif event.key == pygame.K_RIGHT:
                        if self.column < 9:  # Board size, indexed from zero
                            self.organism_go_right()
                        running = False
                    elif event.key == pygame.K_UP:
                        if self.row > 0:
                            self.organism_go_top()
                        running = False
                    elif event.key == pygame.K_DOWN:
                        if self.row < 9:  # Board size, indexed from 0
                            self.organism_go_bottom()
                        running = False

        grid_board[self.row][self.column] = self.character
        self.print_to_journal(f"""({self.row}, {self.column})\n""")

    def collision(self):
        pass

    def get_static_counter(self):
        return 1
