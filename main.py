from flask import Flask, render_template,request,redirect,flash,abort 
import pymysql
from dynaconf import Dynaconf

app = Flask(__name__)

conf = Dynaconf(
    settings_file = {"settings.toml"}
)
class User:
    is_authenticated = True
    is_anonymous = False 
    is_active = True 
    
    def __init__(self, user_id, username, email, first_name, last_name):
        self.id = user_id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def get_id(self):
        return str(self>id)
    
    @login_manager.user_loader 
    def load_user(user_id):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM `Customer` WHERE `id` ={user_id};")

        result = cursor.fetchone()

        cursor.close()
        conn.close()
    
def connect_db():
    conn = pymysql.connect(
        host = "10.100.34.80",
        database="nbristol_tronicsonthelow",
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


@app.route("/product/<product_id>")
def product_page(product_id):
    
    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM `Product` WHERE `id`={product_id}; ")

    result = cursor.fetchone()
    if result is None: 
       abort(404)
    cursor.close()
    conn.close()


    return result

def get_id(self):
    return str(self.id)


   



    @app.route("/product<product_id>")
    def product_page(product_id):""


    @app.route("/signup",methods =["POST", "GET"])
    def sign_up():""


    @app.route("/signup",methods =["POST", "GET"])
    def sign_up():
      if  request.method == "POST":
        username = request.form['username'].strrip()
        password = request.form['password']

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM `Customer` WHERE `username`= `{username};")

        result = cursor.fetchone()

        if result is None:
            flash ("Your username/password is incorrect")
        elif password != result["password"]:
            flash("Your username/password is incorrect")
        else:
            user = user(result["id"], result["username"], result["email"], result["first_name"], result["last_name"])
            
            flask_login.login_user(user)
            
            return redirect('/')
        
        return render_template("signin.html.jinja")
      
    @app.route('/logout')
    def logout():
        flask_login.login_user()
        return redirect ("/")
    
    @app.route