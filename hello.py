# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '''
    <h1>Avaliação contínua: Aula 030</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/user/Julia%20Vilela/PT3031861/IFSP">Identificação</a></li>
        <li><a href="/contextorequisicao">Contexto de requisição</a></li>
    </ul>
    '''

@app.route('/user/<name>/<pt>/<inst>')
def user(name, pt, inst):
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Aluno: {name}</h2>
    <h2>Prontuário: {pt}</h2>
    <h2>Instituição: {inst}</h2>
    '''

@app.route('/contextorequisicao')
def req():
    user_agent = request.headers.get('User-Agent') # informação que o servidor pega para saber do navegador e so
    ip = request.remote_addr
    host = request.host
    return f'''
    <h1>Avaliação contínua: Aula 030</h1>
    <h2>Seu navegador é: {user_agent}</h2>
    <h2>O IP do computador remoto é: {ip}</h2>
    <h2>O host da aplicação é: {host}</h2>
    '''

