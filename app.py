# from flask import Flask, render_template, request, redirect, url_for, session
# import sqlite3

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# # Initialize DB
# def init_db():
#     conn = sqlite3.connect('users.db')
#     conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
#     conn.close()

# @app.route('/')
# def main():
#     username = session.get('username')
#     return render_template('home.html', username=username)
# @app.route('/formals')
# def formals():
#     return render_template('formals.html')
# @app.route('/form1')
# def form1():
#     return render_template('form1.html')
# @app.route('/form2')
# def form2():
#     return render_template('form2.html')
# @app.route('/form3')
# def form3():
#     return render_template('form3.html')
# @app.route('/jackets')
# def jackets():
#     return render_template('jackets.html')
# @app.route('/jac1')
# def jac1():
#     return render_template('jac1.html')
# @app.route('/jac2')
# def jac2():
#     return render_template('jac2.html')
# @app.route('/jac3')
# def jac3():
#     return render_template('jac3.html')
# @app.route('/over')
# def over():
#     return render_template('over.html')
# @app.route('/sleve')
# def sleve():
#     return render_template('sleve.html')
# @app.route('/cargo')
# def cargo():
#     return render_template('cargo.html')
# @app.route('/watches')
# def watches():
#     return render_template('watches.html')
# @app.route('/shoes')
# def shoes():
#     return render_template('shoes.html')
# @app.route('/men')
# def men():
#     return render_template('men.html')
# @app.route('/home')
# # def home():
# #     return render_template('home.html')
# @app.route('/new')
# def new():
#     return render_template('new-arrivals.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('login'))
#     return render_template('signup.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
#         user = cursor.fetchone()
#         conn.close()
#         if user:
#             session['username'] = username
#             return redirect(url_for('main'))
#         else:
#             return "Invalid credentials"
#     return render_template('login.html')


# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('main'))

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize MySQL DB connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="USER_IN"
)
cursor = db.cursor()

@app.route('/')
def main():
    username = session.get('username')
    return render_template('home.html', username=username)

@app.route('/formals')
def formals():
    return render_template('formals.html')

@app.route('/form1')
def form1():
    return render_template('form1.html')

@app.route('/form2')
def form2():
    return render_template('form2.html')

@app.route('/form3')
def form3():
    return render_template('form3.html')

@app.route('/jackets')
def jackets():
    return render_template('jackets.html')

@app.route('/jac1')
def jac1():
    return render_template('jac1.html')

@app.route('/jac2')
def jac2():
    return render_template('jac2.html')

@app.route('/jac3')
def jac3():
    return render_template('jac3.html')

@app.route('/over')
def over():
    return render_template('over.html')
@app.route('/ov1')
def ov1():
    return render_template('ov1.html')
@app.route('/ov2')
def ov2():
    return render_template('ov2.html')
@app.route('/ov3')
def ov3():
    return render_template('ov3.html')

@app.route('/sleve')
def sleve():
    return render_template('sleve.html')
@app.route('/sleve1')
def sleve1():
    return render_template('sleve1.html')
@app.route('/sleve2')
def sleve2():
    return render_template('sleve2.html')
@app.route('/sleve3')
def sleve3():
    return render_template('sleve3.html')
@app.route('/shoes-main')
def shoesmain():
    return render_template('shoes-main.html')
@app.route('/cargo')
def cargo():
    return render_template('cargo.html')
@app.route('/car1')
def car1():
    return render_template('car1.html')
@app.route('/car2')
def car2():
    return render_template('car2.html')
@app.route('/car3')
def car3():
    return render_template('car3.html')

# @app.route('/watches')
# def watches():
#     return render_template('watches.html')
@app.route('/watches')
def watches():
    return render_template('watches.html')
@app.route('/wa1')
def wa1():
    return render_template('wa1.html')
@app.route('/wa2')
def wa2():
    return render_template('wa2.html')
@app.route('/wa3')
def wa3():
    return render_template('wa3.html')
@app.route('/shoes')
def shoes():
    return render_template('shoes.html')
@app.route('/roadster')
def roadster():
    return render_template('roadster.html')
@app.route('/asian')
def asian():
    return render_template('asian.html')
@app.route('/nykaa')
def nykaa():
    return render_template('nykaa.html')
@app.route('/neki')
def neki():
    return render_template('neki.html')
@app.route('/puma')
def puma():
    return render_template('puma.html')

@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/new')
def new():
    return render_template('new-arrivals.html')
@app.route('/fool')
def fool():
    return render_template('fool.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        db.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        if user:
            session['username'] = username
            return redirect(url_for('main'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))
@app.route('/order-success')
def order_success():
    return render_template('order_success.html')
@app.route('/buy-now', methods=['POST'])
def buy_now():
    # Optional: get product ID, simulate order logic
    # product_id = request.form.get('product_id')
    
    # Here you might log the order or store in DB (optional for now)
    
    return redirect(url_for('order_success'))


# @app.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('query')
#     if query:
#         search_term = f"%{query}%"  # Prepare the query term with wildcards
#         cursor.execute("SELECT * FROM products WHERE name LIKE %s LIMIT 3", (search_term,))
#         results = cursor.fetchall()
#         return render_template('search_results.html', query=query, results=results)
#     return redirect(url_for('main'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip().lower()

    # Redirect to specific pages for known categories
    category_routes = {
        'formals': 'formals',
        'cargo': 'cargo',
        'cargos': 'cargo',
        'jackets': 'jackets',
        'shoes': 'shoes',
        'watches': 'watches',
        'men': 'men',
        'new arrivals': 'new',
        'new': 'new',
        'over': 'over',
        'oversized': 'over',
        'sleeve': 'sleve',
        'sleve': 'sleve',
        'shirts':'sleve',
        'shoes': 'puma'
    }

    if query in category_routes:
        return redirect(url_for(category_routes[query]))

    # Otherwise, do a product search (e.g., brand like "Puma")
    # search_term = f"%{query}%"
    # cursor.execute("SELECT * FROM products WHERE name LIKE %s LIMIT 3", (search_term,))
    # results = cursor.fetchall()
    # return render_template('search_results.html', query=query, results=results)



if __name__ == '__main__':
    app.run(debug=True)
