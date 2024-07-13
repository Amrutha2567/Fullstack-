from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/toggle-publish/<int:dishId>', methods=['POST'])
def toggle_publish(dishId):
    conn = get_db_connection()
    dish = conn.execute('SELECT * FROM dishes WHERE dishId = ?', (dishId,)).fetchone()
    new_status = not dish['isPublished']
    conn.execute('UPDATE dishes SET isPublished = ? WHERE dishId = ?', (new_status, dishId))
    conn.commit()
    conn.close()
    socketio.emit('status_update', {'dishId': dishId, 'newStatus': new_status})
    return jsonify({'dishId': dishId, 'newStatus': new_status})

if __name__ == '__main__':
    socketio.run(app, debug=True)
