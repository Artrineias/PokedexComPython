import requests

def name(pokemon):
    nome = json_do_pokemon(pokemon)
    if nome != None:
        return nome['name']
    else:
        return nome    


def id(pokemon):
    ide = json_do_pokemon(pokemon)
    if ide != None:
        return ide['id']
    else:
        return ide


def tipo(pokemon):
    tipos = json_do_pokemon(pokemon)
    info_str= ""
    if tipos != None:    
        for i in tipos['types']:
            info_str +=f"{i['type']['name']}\n"
        return info_str
    else:
        return tipos


def abilities(pokemon):
    habilidades =json_do_pokemon(pokemon)
    info_str = ""
    if habilidades != None:
        for i in habilidades['abilities']:
            info_str += f"{i['ability']['name']}\n"
        return info_str
    else:
        return habilidades


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
    nome = "pikahhu"
    
    print(name(nome))
    print(id(json_do_pokemon(nome)))
    print(abilities(nome))
    print(tipo(nome))