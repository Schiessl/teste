from flask import Flask, render_template

app = Flask(__name__) #cria o site vazio

#criar a 1º pagina do site
# route -> caminho do site - agoravai.com.br
@app.route("/")

# função -> o que exibir naquela página
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/tabelas")
def tabelas():
    return render_template("tabelas.html")

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) # debug=True manter o site no ar sem reinicialização