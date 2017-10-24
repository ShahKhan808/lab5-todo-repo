from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL
 
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abdullah'
app.config['MYSQL_DB'] = 'todolist'
app.config['MYSQL_HOST'] = '35.187.103.1'
mysql.init_app(app)
