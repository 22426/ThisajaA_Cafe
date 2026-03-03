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
    query = "SELECT * FROM products WHERE cat_id=?"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query, (cat_id, ))
    results = cur.fetchall()
    print(results)
    con.close()
    return render_template('menu.html', results=results)


@app.route('/contact')
def render_contact_page():
    return render_template('contact.html')


app.run(host='0.0.0.0', debug=True)
