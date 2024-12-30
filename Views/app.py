from flask import Flask, render_template, request, jsonify, session
import requests
import uuid

app = Flask(__name__)
app.secret_key = "sk"

CHATBOT_API_URL = "http://localhost:8000/get_response"

@app.route("/")
def index():
    session_id = session.get("session_id")

    if session_id is None:
        session["session_id"] = str(uuid.uuid4())
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
        response = requests.post(
            CHATBOT_API_URL,
            json={
                "query": msg
            },
        )

        return jsonify({"response": response.json()["response"]})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5050, host="0.0.0.0")
