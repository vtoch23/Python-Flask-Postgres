from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database="flask_db", 
    user="Vanya",
    password="123456789", 
    host="localhost", 
    port="5432")
print('connected')
cur = conn.cursor()


cur.execute(
    '''CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), price float);''')


conn.commit()

cur.close()
conn.close()


@app.route('/')
def index():
    conn = psycopg2.connect(database="flask_db", user="Vanya",
                            password="123456789", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute('''SELECT * FROM products''')

    data = cur.fetchall()

    cur.close()
    conn.close()
    return render_template('index.html', data=data)


@app.route('/create', methods=['POST'])
def create():
    conn = psycopg2.connect(database="flask_db", user="Vanya",
                            password="123456789", host="localhost", port="5432")

    print('connected')

    cur = conn.cursor()

    name = request.form['name']
    price = request.form['price']

    cur.execute(
        '''INSERT INTO products (name, price) VALUES (%s, %s)''', (name, price))

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update():
    conn = psycopg2.connect(database="flask_db",
                            user="Vanya",
                            password="123456789",
                            host="localhost", port="5432")

    cur = conn.cursor()

    name = request.form['name']
    price = request.form['price']
    id = request.form['id']

    cur.execute(
        '''UPDATE products SET name=%s, price=%s WHERE id=%s''', (name, price, id))

    conn.commit()
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    conn = psycopg2.connect(database="flask_db",
                            user="Vanya",
                            password="123456789",
                            host="localhost", port="5432")

    cur = conn.cursor()
    id = request.form['id']

    cur.execute('''DELETE FROM products WHERE id=%s''', (id,))

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
