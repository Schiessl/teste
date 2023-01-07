from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira ppagina do site
    # route -> hashtagtreinamento.com/contatos
    # função-> o que você quer exibir naquela página
@app.route("/") 
def homepage():
    return "teste do site"

@app.route('/inscrito/<nome_inscrito>')
def inscrito(nome_inscrito):
    return f'Olá {nome_inscrito}' 

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)