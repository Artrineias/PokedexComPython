from flask import Flask,render_template

def inicial():

    site = Flask(__name__)
    
    @site.route("/")
    def index():
        return render_template("index.html")
    
    @site.route("/<string:digitado>")
    def erro(digitado):
        return render_template("html/erro.html")

    
    return site

if __name__=="__main__":
    inicial()    

