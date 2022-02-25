from flask import Flask,render_template
import pokemon
import requests

def inicial():

    site = Flask(__name__)
    
    @site.route("/")
    def index():
        return render_template("html/index.html")

    
    @site.route("/pikachu/")
    def lista():
        nome = "pikachu"
        name = pokemon.name(nome)
        ide = pokemon.id(nome)
        tipo = pokemon.tipo(nome)
        habilidade = pokemon.abilities(nome)
        return render_template("html/pokemon.html", nome = name, id = ide , type= tipo ,abilities = habilidade   )

    
    @site.route("/<string:digitado>")
    def erro(digitado):
        return render_template("html/erro.html")

    
    return site

if __name__=="__main__":
    inicial()    

