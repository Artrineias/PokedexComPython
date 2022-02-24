import requests

def name(pokemon):
    return pokemon['name']
    

def id(pokemon):
    return pokemon['id']
    
    
def tipo(pokemon):
    info_str= ""
    for i in pokemon['types']:
        info_str +=f"{i['type']['name']}\n"
    return info_str
    

def abilities(pokemon):
    info_str = ""
    for i in pokemon['abilities']:
        info_str += f"{i['ability']['name']}\n"
    return info_str


def json_do_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    ficha = (requests.get(url)).json()

    return ficha


if  __name__ =="__main__":
    print(id(json_do_pokemon("pikachu")))