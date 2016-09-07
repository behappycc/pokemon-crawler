import re
import json

import util

def read_pokemonid():
    # data -> http://www.pokemon.com/us/pokedex/
    list_pokemons = []
    pokemons = {}

    with open("id.txt", 'r', encoding='utf-8') as datafile:
        for line in datafile:
            if line != '\n':
                pokemon = {}
                temp = line.replace('\n', '').split(' ')
                list_pokemons.append([temp[0], int(temp[1])])

        for i, pokemon  in enumerate (list_pokemons):
            pokemons[i+1] = pokemon[0]

        util.write_json(pokemons, 'id.json')

def main():
    read_pokemonid()

if __name__ == '__main__':
    main()