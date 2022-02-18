from flask import Flask,render_template

site = Flask(__name__)

@site.route("/")
def index():
    return render_template("index.html")


@site.route("/lista/")
def lista():
    return render_template("lista.html")


if __name__=="__main__":
    pass    


def inicial():    
    site.run(debug=True)

