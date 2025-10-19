from flask import Flask, jsonify

app = Flask(__name__, static_folder="public", static_url_path="/public")

@app.route("/")
def home():
    return "Hello, Flask is working!!!!!"

@app.route("/api/v1/cat", methods=["GET"])
def get_cat():
    cat = {
  "cat_id": 1,
  "cat_name": "Fluffy",
  "weight": 5,
  "owner": "1",
  "owner_name": "John Doe",
  "birthdate": "2020-01-01",
  "filename": "cat.jpg"  
    }
    return jsonify(cat)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
