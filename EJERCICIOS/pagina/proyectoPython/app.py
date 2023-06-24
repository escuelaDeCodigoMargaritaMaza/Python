from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'yaelmago'
app.config['MYSQL_DB'] = 'baseusuarios'

mysql = MySQL(app)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (nombre_usuario, contraseña) VALUES (%s, %s)", (nombre_usuario, contraseña))
        mysql.connection.commit()
        cur.close()
        
        return 'Registro exitoso!'
    
    return render_template('registro.html')

if __name__ == '__main__':
    app.run()