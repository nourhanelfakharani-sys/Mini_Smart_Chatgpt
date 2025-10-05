from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index_backend.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "").lower()

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

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)



    



    



