from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = 'cafe_db'

app = Flask(__name__)

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        print("There was an error connecting to the database")
        return None


@app.route('/')
def render_homepage():
    return render_template('home.html')


@app.route('/menu/<cat_id>')
def render_menu_page(cat_id):
    con = create_connection(DATABASE)
    query = "SELECT * FROM products WHERE fk_cat_id=?"
    query_2 = "SELECT * FROM categories"
    cur = con.cursor()
    cur.execute(query, (cat_id, ))
    results = cur.fetchall()
    cur = con.cursor()
    cur.execute(query_2)
    cat_results = cur.fetchall()
    con.close()
    return render_template('menu.html', results=results, cat_results=cat_results)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
