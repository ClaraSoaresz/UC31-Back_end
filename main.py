from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inscricao', methods=['GET', 'POST'])
def inscricao():
    mensagem = ""

    if request.method == 'POST':
        nickname = request.form.get