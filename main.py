from flask import Flask,render_template

def inicial():

    site = Flask(__name__)
    
    @site.route("/")
    def index():
        return render_template("index.html")


    @site.route("/lista/")
    def lista():
        return render_template("lista.html")

    
    return site




if __name__=="__main__":
    inicial()    

