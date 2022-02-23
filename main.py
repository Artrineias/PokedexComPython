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
        x = "pikachu"
        name = pokemon.name(x)
        ide = pokemon.id(x)
        tipo = pokemon.tipo(x)
        habilidade = pokemon.abilities(x)
        return render_template("html/pokemon.html", nome = name, id = ide , type= tipo ,abilities = habilidade   )

    
    @site.route("/<string:digitado>")
    def erro(digitado):
        return render_template("html/erro.html")

    
    return site

if __name__=="__main__":
    inicial()    

