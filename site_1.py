from flask import Flask, render_template

#render template é uma funcionalidade que se importa do flask para renderizar os templates criados

app = Flask(__name__)

#criar uma pagina
#toda pagina tem um route e uma função
# a route define o direcionamento do caminho depois do dominio
#a função define o que vai aparecer na página

@app.route("/") #esse decorator atribui uma funcionalidade pra função abaixo dela
def homepage():
    return render_template("homepage.html") 

@app.route("/contatos")
def contatos():
    return render_template("contatos.html") 


#criação de pagina dinamica

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #ativando o debugar do site - assim, todas as edições serão feitas automaticamente sem precisar parar e e rodar o codigo de novo

