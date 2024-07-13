from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('dishes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/dishes', methods=['GET'])
def get_dishes():
    conn = get_db_connection()
    dishes = conn.execute('SELECT * FROM dishes').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in dishes])

@app.route('/toggle-publish/<int:dishId>', methods=['POST'])
def toggle_publish(dishId):
    conn = get_db_connection()
    dish = conn.execute('SELECT * FROM dishes WHERE dishId = ?', (dishId,)).fetchone()
    new_status = not dish['isPublished']
    conn.execute('UPDATE dishes SET isPublished = ? WHERE dishId = ?', (new_status, dishId))
    conn.commit()
    conn.close()
    return jsonify({'dishId': dishId, 'newStatus': new_status})

if __name__ == '__main__':
    app.run(debug=True)
