import requests

class NameOrId:
    def __init__(self,nome="pikachu"):
        self.name = name((nome.lstrip('0')))
        self.id = id(nome.lstrip('0'))
        self.type = tipo((nome.lstrip('0')))
        self.weight = Weight(nome.lstrip('0'))
        self.height = height(nome.lstrip('0'))
        self.abilities = abilities((nome.lstrip('0')))
        self.image = imagens(nome.lstrip('0'))

    


def name(pokemon):
    nome = jsonPokemon(pokemon)
    if nome != None:
        return nome['name']
    else:
        return "???"   

def imagens(pokemon):
    img = jsonPokemon(pokemon)
    if img != None:
        if int(id(pokemon))<9:
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/00{id(pokemon)}.png"
        elif int(id(pokemon))<99:
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/0{id(pokemon)}.png"
        else:
            return f"https://assets.pokemon.com/assets/cms2/img/pokedex/full/{id(pokemon)}.png"
    else:
        return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png"

def Weight(pokemon):
    peso = jsonPokemon(pokemon)
    if peso != None:
        return f"{int(peso['weight'])/10} kg"
    else:
        return "???"   

def id(pokemon):
    ide = jsonPokemon(pokemon)
    if ide != None:
        return ide['id']
    else:
        return "???"

def tipo(pokemon):
    tipos = jsonPokemon(pokemon)
    info_str= ""
    if tipos != None:    
        for i in tipos['types']:
                info_str +=f"[{i['type']['name']}]"
        return info_str
    else:
        return "???"

def height(pokemon):
    altura = jsonPokemon(pokemon)
    if altura != None:    
        return f"{int(altura['height'])/10} m"
    else:
        return "???"

def abilities(pokemon):
    habilidades =jsonPokemon(pokemon)
    info_str = ""
    if habilidades != None:
        for i in habilidades['abilities']:
            info_str += f"[{i['ability']['name']}]"
        return info_str
    else:
        return "???"


def verificadorJson(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    if str(requests.get(url)) == "<Response [404]>" or name =="":
        return False
    else:
        return True


def jsonPokemon(name):
    
    if verificadorJson(name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        ficha = (requests.get(url)).json()
        return ficha
    else:
        return None


if  __name__ =="__main__":
    nome = "ajdoaslofv"
    
    print(name(nome))
    print(id(nome))
    print(abilities(nome))
    print(tipo(nome))
    print(height(nome))
    print(Weight(nome))
    print(imagens(nome))