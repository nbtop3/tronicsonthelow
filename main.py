from flask import Flask, render_template
import pymysql
from dynaconf import Dynaconf

app = Flask(__name__)

conf = Dynaconf(
    settings_file = {"settings.toml"}
)
def connect_db():
    conn = pymysql.connect(
        host = "10.100.34.80",
        database="nbristol_appleonthelow",
        user ='nbristol',
        password = conf.password,
        autocommit = True,
        cursorclass = pymysql.cursors.DictCursor
    )

@app.route("/")
def index():
    return render_template("homepage.html.jinja")
    
@app.route("/browse")
def product_browse():
    query = request.args.get('query')

    conn = connect_db()

    cursor = conn.cursor()

    if query is None:
        cursor.excute("SELECT * FROM `Product`;")
    
    cursor.excute(f"SELECT * FROM `Product` WHERE `name` LIKE '%{query}%' ;")

    result = cursor.fetchall()
   
   
    cursor.close()
    conn.close()


    return render_template("browse.html.jinja",)