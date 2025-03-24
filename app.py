from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, é isso AI! CI/CD"

if __name__ == '__main__':
    app.run(debug=True)
