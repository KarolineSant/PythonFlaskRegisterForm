from flask import Flask, render_template, request, jsonify
import MySQLdb.cursors
from sqlalchemy import text, engine_from_config
from config import config
  
app = Flask(__name__)
  
engine = engine_from_config(config, prefix='db.')
# app.secret_key = 'your secret key'
  
app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'b65728e0f39982'
app.config['MYSQL_PASSWORD'] = '35d923f8'
app.config['MYSQL_DB'] = 'heroku_d8999df6c664795'

@app.route('/', methods =['GET'])
def home():
    return render_template('register.html')
  
@app.route('/register', methods =['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    cep = request.form['cep']
    logradouro = request.form['logradouro']
    numero = request.form['numero']
    complemento = request.form['complemento']
    bairro = request.form['bairro']
    with engine.connect() as con:
        statement = text("""INSERT INTO cad_alunos 
            (nome, email, cep, logradouro, numero, complemento, bairro) values
            (:nome, :email, :cep, :logradouro, :numero, :complemento, :bairro)""")
        con.execute(statement, nome=nome, email=email, cep=cep, logradouro=logradouro, numero=numero, complemento=complemento, bairro=bairro)
    return "ok"

@app.route('/list', methods =['GET'])
def list():
    with engine.connect() as con:
        statement = text("""SELECT nome, email, cep, logradouro, numero, complemento, bairro 
                            FROM cad_alunos""")
        rs = con.execute(statement)
        pagamento = []
        item = rs.fetchone()
        while (item != None):
            pagamento.append(dict(item))
            item = rs.fetchone()
    return jsonify(pagamento)


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)