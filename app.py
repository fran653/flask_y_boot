from flask import Flask, render_template
#creo instancia de flask
app = Flask(__name__)
titulo_app = 'Puto BASIC fit'
@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url http://localhost:5000/index.html añado otra ruta más
def inicio(): #en modo debug se ven cambios de forma automática
    app.logger.debug('entramos al path de inicio /')
    return render_template('index.html', titulo = titulo_app) #renderiza el template index.html

if __name__ =='__main__':
    app.run(debug=True)