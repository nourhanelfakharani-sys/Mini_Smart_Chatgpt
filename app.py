from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(_name_, template_folder="templates")

# --- Database connection ---
def get_db_connection():
    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

# --- Ensure tables exist ---
conn = get_db_connection()
cursor = conn.cursor()

# users table (لو مش متعمل قبل كده)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")

# messages table linked to users
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    sender TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
""")

conn.commit()
conn.close()

# --- Home route ---
@app.route("/")
def home():
    return render_template("index_backend.html")

# --- Chat route ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").lower()

    # temporary: fix user_id = 1 (ممكن تخليها متغير بعدين حسب اليوزر)
    user_id = 1

    # Bot response logic
    if "hello" in user_msg or "hi" in user_msg:
        reply = "Hello! How are you doing today?"
    elif "how are you" in user_msg:
        reply = "I'm doing great, thanks for asking! And you?"
    elif "name" in user_msg:
        reply = "I'm your Smart Mini GPT assistant 🤖."
    elif "weather" in user_msg:
        reply = "I can't check the weather right now, but I hope it's nice where you are!"
    elif "bye" in user_msg:
        reply = "Goodbye! Talk to you soon."
    else:
        reply = "Hmm... that's interesting! Can you explain more?"

    # Save messages in DB with user_id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (user_id, sender, message) VALUES (?, ?, ?)", (user_id, "user", user_msg))
    cursor.execute("INSERT INTO messages (user_id, sender, message) VALUES (?, ?, ?)", (user_id, "bot", reply))
    conn.commit()
    conn.close()

    return jsonify({"reply": reply})

# --- Route to fetch all messages ---
@app.route("/all_messages", methods=["GET"])
def all_messages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT messages.id, users.name, messages.sender, messages.message, messages.timestamp
        FROM messages
        JOIN users ON messages.user_id = users.id
        ORDER BY messages.timestamp
    """)
    messages = cursor.fetchall()
    conn.close()

    messages_list = [dict(msg) for msg in messages]
    return jsonify({"messages": messages_list})

# --- Run the app ---
if _name_ == "_main_":
    app.run(debug=True)








