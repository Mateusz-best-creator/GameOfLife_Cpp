#pragma once

#include <vector>
#include "organism.h"

const int KINDS_OF_ORGANISMS = 12;

class World
{
private:
    std::vector<Organism*> organisms;
    int height, width, number_of_organisms, turn = 1;
    const int max_organisms;
    char** board;
    bool is_human_on_map = true;

protected:
    enum ActionType : char { PLAY = 'p', QUIT = 'q', SAVE_GAME = 's', OPEN_GAME = 'o' };

public:
    World(int, int);
    ~World();

    void initialize_game();
    bool makeTurn();
    void play();

    void legend();
    void update_world();
    void drawWorld() const;
    void new_game();

    void sort_organisms();
    
    void add(const std::string&, int times, bool is_animal = true, bool is_human = false);

    int get_strength_at_square(int, int);

    // Functions for loading and reading from file
    void save_game();
    void load_game();
};