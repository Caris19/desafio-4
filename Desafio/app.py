from flask import Flask, render_template, request
import mariadb

try:
    connection = mariadb.connect(
        user="root",
        password="124879",
        host="127.0.0.1",
        port=3306,
        database = "desafio"
    )
except mariadb.Error as e:
   print(f"Error connecting to the database: {e}")

app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quem_somos():
    return render_template("quemsomos.html")

@app.route('/contato', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
        connection.commit()
        return 'Enviado'
    return render_template('contato.html')

@app.route('/users')
def users():
    cursor = connection.cursor()

    users = cursor.execute("SELECT * FROM contatos")

    if users !='':
        userDetails = cursor.fetchall()

        return render_template("usuarios.html", userDetails=userDetails)