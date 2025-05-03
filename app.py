from flask import Flask
#creo instancia de flask
app = Flask(__name__)
@app.route('') #url: http://localhost:5000/
def inicio():
    app.logger.debug('entramos al path de inicio /')
    return '<>hola negro </p>'

if __name__ =='__main__':
    app.run(debug=True)