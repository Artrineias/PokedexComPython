import requests

class NameOrId:
    def __init__(self,nome):
        self.name = name((nome.lstrip('0')))
        self.id = id((nome.lstrip('0')))
        self.type = tipo((nome.lstrip('0')))
        self.weight = Weight((nome.lstrip('0')))
        self.height = height((nome.lstrip('0')))
        self.abilities = abilities((nome.lstrip('0')))
        self.image = imagens((nome.lstrip('0')))

    


def name(pokemon):
    nome = json_do_pokemon(pokemon)
    if nome != None:
        return nome['name']
    else:
        return "???"   

def imagens(pokemon):
    img = json_do_pokemon(pokemon)
    if img != None:
        return img['sprites']['front_default']
    else:
        return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png"
def Weight(pokemon):
    peso = json_do_pokemon(pokemon)
    if peso != None:
        return f"{int(peso['weight'])/10} kg"
    else:
        return "???"   

def id(pokemon):
    ide = json_do_pokemon(pokemon)
    if ide != None:
        return ide['id']
    else:
        return "???"

def tipo(pokemon):
    tipos = json_do_pokemon(pokemon)
    info_str= ""
    if tipos != None:    
        for i in tipos['types']:
                info_str +=f"[{i['type']['name']}]"
        return info_str
    else:
        return "???"

def height(pokemon):
    altura = json_do_pokemon(pokemon)
    if altura != None:    
        return f"{int(altura['height'])/10} m"
    else:
        return "???"

def abilities(pokemon):
    habilidades =json_do_pokemon(pokemon)
    info_str = ""
    if habilidades != None:
        for i in habilidades['abilities']:
            info_str += f"[{i['ability']['name']}]"
        return info_str
    else:
        return "???"


def verificador(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    if str(requests.get(url)) == "<Response [404]>":
        return False
    else:
        return True


def json_do_pokemon(name):
    
    if verificador(name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        ficha = (requests.get(url)).json()
        return ficha
    else:
        return None


if  __name__ =="__main__":
    nome = "pikachu"
    
    print(name(nome))
    print(id(nome))
    print(abilities(nome))
    print(tipo(nome))
    print(height(nome))
    print(Weight(nome))
    print(imagens(nome))