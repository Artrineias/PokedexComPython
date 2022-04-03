from flask import Flask,render_template,request
from pokemon import NameOrId
def inicial():

    site = Flask(__name__)
    
    @site.route("/",methods=["GET","POST"])
    def index(): 
        
        if request.method == "POST":
            name = request.form.get("name")
        else:
            name = "pikachu" 
        poke = NameOrId(name)
        return render_template("index.html",
                name=poke.name,id=poke.id,
                type=poke.type,abilities=poke.abilities,
                height=poke.height,weight=poke.weight,
                img=poke.image
                )
    
    @site.route("/<string:digitado>")
    def erro(digitado):
        return render_template("html/erro.html")

    
    return site

if __name__=="__main__":
    inicial()    

