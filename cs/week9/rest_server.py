import sqlite3
from flask import Flask, request, jsonify
import datetime as dt

app = Flask(__name__)
DB_NAME = "messages.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT,
                timestamp TEXT
            )
        ''')
        conn.commit()

@app.route('/stats', methods=['GET'])
def get_stats():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM history")
        count = cursor.fetchone()[0]
        
        cursor.execute("SELECT timestamp FROM history ORDER BY id DESC LIMIT 1")
        last_time = cursor.fetchone()
        
    return jsonify({
        "total_messages_in_db": count,
        "last_activity": last_time[0] if last_time else "No activity"
    }), 200

@app.route('/history', methods=['GET'])
def get_history():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row 
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, message, timestamp FROM history ORDER BY id DESC LIMIT 10")
        rows = cursor.fetchall()
        
        history_list = []
        for row in rows:
            history_list.append({
                "id": row["id"],
                "message": row["message"],
                "time": row["timestamp"]
            })
            
    return jsonify(history_list), 200

@app.route('/send', methods=['POST'])
def handle_message():
    data = request.get_json()
    rcvmsg = data.get("message", "")
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (message, timestamp) VALUES (?, ?)", (rcvmsg, now))
        conn.commit()

    return jsonify({"status": "saved", "message": rcvmsg}), 200

if __name__ == '__main__':
    init_db()
    app.run(port=65432, debug=True)