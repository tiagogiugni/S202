from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
    def __init__(self, database, collection):
        self.db = Database(database, collection)

    '''Query 1'''
    def getPokemonsByType(types: list):
        return db.collection.find({"type": {"$in": types}})

    types = ["Poison"]
    pokemons = getPokemonsByType(types)
    writeAJson(pokemons, "pokemons_by_type")  

    '''Query 2'''
    def getPokemonByName(name: str):
        return db.collection.find({"name": name})

    charmander = getPokemonByName("Charmander")
    writeAJson(charmander, "charmander")

    '''Query 3'''
    def getPokemonWithoutMultiplier():
        pokemons = db.collection.find({"multipliers": {"$exists": False}})
        writeAJson(pokemons, "pokemons_without_multiplier")

    '''Query 4'''
    def getPokemonsByTypes(types: list):
        return db.collection.find({"type": {"$in": types}})

    types = ["Grass", "Water"]
    pokemons = db.collection.find({ "type": {"$in": types}, "next_evolution": {"$exists": True} })
    writeAJson(pokemons, "pokemons_by_types")

    '''Query 5'''
    def getPokemonsByWeakness(weaknesses: list):
        return db.collection.find({"type": {"$in": weaknesses}})
    
    weaknesses = ["Psychic", "Ice"]
    pokemons = db.collection.find({"weaknesses": {"$all": weaknesses}})
    writeAJson(pokemons, "pokemon5_by_weaknesses")  