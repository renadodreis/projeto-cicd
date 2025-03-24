from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
      <head>
         <style>
           body {
             background-color: #f0f8ff; 
             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
           }
         </style>
      </head>
      <body>
         <h1>Olá, CI/CD  Deployado! </h1>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
