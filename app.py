from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return '"Alô Mundo ! Aqui é o Thiago vidal testando o Flask !'

app.run()
